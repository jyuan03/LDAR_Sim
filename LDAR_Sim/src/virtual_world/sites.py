# ------------------------------------------------------------------------------
# Program:     The LDAR Simulator (LDAR-Sim)
# File:        sites
# Purpose:     The sites module. Pregenerate sites and regenerate sites
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published
# by the Free Software Foundation, version 3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# MIT License for more details.

# You should have received a copy of the MIT License
# along with this program.  If not, see <https://opensource.org/licenses/MIT>.
#
# ------------------------------------------------------------------------------

import copy
from datetime import date
import math


import pandas as pd
from file_processing.output_processing.output_utils import TsEmisData
from file_processing.input_processing.emissions_source_processing import (
    EmissionsSource,
)
from scheduling.schedule_dataclasses import TaggingInfo
from virtual_world.emissions import Emission
from virtual_world.equipment_groups import Equipment_Group

from virtual_world.infrastructure_const import (
    Infrastructure_Constants,
)

PLACEHOLDER_EQUIPMENT = "Placeholder_Equipment"
PLACEHOLDER_EQUIPMENT_COUNT = 10


class Site:
    # TODO its lat and lon not lat and long
    def __init__(
        self,
        id: str,
        lat: float,
        long: float,
        equipment_groups: list,
        propagating_params: dict,
        infrastructure_inputs: dict,
        start_date: date,
        methods: list[str],
        site_type: str = None,
    ) -> None:
        self._site_ID: str = id
        self._lat: float = lat
        self._long: float = long

        self._site_type: str = site_type
        # TODO check that we use these
        self._survey_frequencies: dict = propagating_params["Method_Specific_Params"].pop(
            Infrastructure_Constants.Sites_File_Constants.SURVEY_FREQUENCY_PLACEHOLDER
        )
        self._deployment_months = propagating_params["Method_Specific_Params"].pop(
            Infrastructure_Constants.Sites_File_Constants.DEPLOYMENT_MONTHS_PLACEHOLDER
        )
        self._deployment_years = propagating_params["Method_Specific_Params"].pop(
            Infrastructure_Constants.Sites_File_Constants.DEPLOYMENT_YEARS_PLACEHOLDER
        )
        self._create_equipment_groups(equipment_groups, infrastructure_inputs, propagating_params)
        self._set_survey_costs(methods=methods)
        self._latest_tagging_survey_date: date = start_date

    def _create_equipment_groups(
        self, equipment_groups: list, infrastructure_inputs, propagating_params
    ) -> None:
        self._equipment_groups: list[Equipment_Group] = []
        if isinstance(equipment_groups, list) and len(equipment_groups) > 0:
            equip_groups_in: pd.DataFrame = infrastructure_inputs["equipment_groups"]
            for equipment_group in equipment_groups:
                site_equipment_group = equip_groups_in.loc[
                    equip_groups_in[
                        Infrastructure_Constants.Equipment_Group_File_Constants.EQUIPMENT_GROUP
                    ]
                    == equipment_group
                ].iloc[0]
                prop_params = copy.deepcopy(propagating_params)
                self._equipment_groups.append(
                    Equipment_Group(
                        site_equipment_group[
                            Infrastructure_Constants.Equipment_Group_File_Constants.EQUIPMENT_GROUP
                        ],
                        infrastructure_inputs,
                        prop_params,
                        site_equipment_group,
                    )
                )
        elif isinstance(equipment_groups, (int, float)):
            for i in range(0, int(equipment_groups)):
                equip_group_info = pd.Series(
                    {
                        PLACEHOLDER_EQUIPMENT: math.ceil(
                            PLACEHOLDER_EQUIPMENT_COUNT / equipment_groups
                        )
                    }
                )
                prop_params = copy.deepcopy(propagating_params)
                self._equipment_groups.append(
                    Equipment_Group(i, infrastructure_inputs, prop_params, equip_group_info)
                )
        else:
            # REVIEW: Should this be an elif and have an else that does error handling for bad input
            equip_group_info = pd.Series(
                {PLACEHOLDER_EQUIPMENT: math.ceil(PLACEHOLDER_EQUIPMENT_COUNT)}
            )
            prop_params = copy.deepcopy(propagating_params)
            self._equipment_groups.append(
                Equipment_Group(i, infrastructure_inputs, prop_params, equip_group_info)
            )

    def _set_survey_costs(self, methods: list[str]) -> float:
        self._survey_costs: dict[str, float] = {}
        for method in methods:
            self._survey_costs[method] = 0
            for eqg in self._equipment_groups:
                self._survey_costs[method] += eqg.get_survey_cost(method)

    def activate_emissions(self, date: date, sim_number: int) -> int:
        """Activate any emissions that are due to begin on the current date for the given simulation
        and add them to the active emissions list for the equipment at which they occur.

        Args:
            date (date): The current date in simulation.
            sim_number (int): The simulation number.
            Used to interact with the correct set of emissions.
        """
        new_emissions: int = 0
        for eqg in self._equipment_groups:
            new_emissions += eqg.activate_emissions(date, sim_number)
        return new_emissions

    def generate_emissions(
        self,
        sim_start_date,
        sim_end_date,
        sim_number,
        emission_rate_source_dictionary: dict[str, EmissionsSource],
        repair_delay_dataframe: pd.DataFrame,
    ) -> dict:
        site_emissions: dict = {}
        for eqg in self._equipment_groups:
            eqg: Equipment_Group
            site_emissions.update(
                eqg.generate_emissions(
                    sim_start_date,
                    sim_end_date,
                    sim_number,
                    emission_rate_source_dictionary,
                    repair_delay_dataframe,
                )
            )

        return {self._site_ID: site_emissions}

    def get_detectable_emissions(self, method_name: str) -> dict[str, dict[str, list[Emission]]]:
        detectable_emissions: dict[str, dict[str, Emission]] = {}
        for eqg in self._equipment_groups:
            detectable_emissions[eqg.get_id()] = eqg.get_detectable_emissions(method_name)

        return detectable_emissions

    def get_required_surveys(self, method_name) -> int:
        return self._survey_frequencies[method_name]

    def get_method_survey_time(self, method_name) -> float:
        survey_time: float = 0
        for eqg in self._equipment_groups:
            survey_time += eqg.get_survey_time(method_name=method_name)
        return survey_time

    def get_id(self) -> str:
        return self._site_ID

    def get_loc(self) -> tuple[float, float]:
        return self._lat, self._long

    # def _get_days_since_last_survey(self, method_name: str, current_date: date) -> int:
    #     return (self._last_survey_dates[method_name] - current_date).days

    # def _get_current_yearly_surveys(self, method_name: str) -> int:
    #     return self._surveys_this_year[method_name]

    def get_latest_tagging_survey_date(self) -> date:
        return self._latest_tagging_survey_date

    def get_emis_data(self) -> pd.DataFrame:
        emis_data: pd.DataFrame = pd.concat([eqg.get_emis_data() for eqg in self._equipment_groups])
        emis_data["Site ID"] = self._site_ID
        return emis_data

    def get_survey_cost(self, method_name: str) -> float:
        return self._survey_costs[method_name]

    def set_latest_tagging_survey_date(self, date: date) -> None:
        self._latest_tagging_survey_date = date

    def set_pregen_emissions(self, site_emissions, sim_number) -> None:
        for eqg in self._equipment_groups:
            eqg.set_pregen_emissions(site_emissions[eqg.get_id()], sim_number)

    def tag_emissions_at_equipment(
        self, equipment_group: str, equipment: str, tagging_info: TaggingInfo
    ) -> None:
        target_equip_group: Equipment_Group | None = next(
            (
                equip_group
                for equip_group in self._equipment_groups
                if equip_group.get_id() == equipment_group
            ),
            None,
        )
        target_equip_group.tag_emissions_at_equipment(equipment, tagging_info)

    def update_emissions_state(self) -> TsEmisData:
        emis_data = TsEmisData()
        for eqg in self._equipment_groups:
            emis_data += eqg.update_emissions_state()
        return emis_data