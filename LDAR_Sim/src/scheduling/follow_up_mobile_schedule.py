"""
------------------------------------------------------------------------------
Program:     The LDAR Simulator (LDAR-Sim)
File:        follow_up_mobile_schedule
Purpose: The extended schedule module, made for follow up schedules

This program is free software: you can redistribute it and/or modify
it under the terms of the MIT License as published
by the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
MIT License for more details.
You should have received a copy of the MIT License
along with this program.  If not, see <https://opensource.org/licenses/MIT>.

------------------------------------------------------------------------------
"""
from datetime import date
from scheduling.follow_up_survey_planner import FollowUpSurveyPlanner
from scheduling.generic_schedule import GenericSchedule
from utils.queue import PriorityQueueWithFIFO
from virtual_world.sites import Site


class FollowUpMobileSchedule(GenericSchedule):
    """A schedule class to provide scheduling functionality for follow-up methods classified
    as the "mobile" type. Will overwrite GenericSchedule functionality as required.
    """

    DEPLOY_TYPE_CODE = "mobile"

    def __init__(
        self,
        method_name: str,
        sites: "list[Site]",
        sim_start_date: date,
        sim_end_date: date,
        est_meth_daily_surveys: int,
        method_avail_crews: int,
    ) -> None:
        super().__init__(
            method_name,
            sites,
            sim_start_date,
            sim_end_date,
            est_meth_daily_surveys,
            method_avail_crews,
        )
        self._site_IDs_in_queue: dict[str, bool] = {
            site.get_id(): False for site in sites
        }
        return

    def get_site_id_queue_list(self) -> dict[str, bool]:
        return self._site_IDs_in_queue

    def get_plan_from_queue(self, site_id: str) -> FollowUpSurveyPlanner:
        new_queue: PriorityQueueWithFIFO = PriorityQueueWithFIFO()
        target_plan: FollowUpSurveyPlanner = None
        while not self._survey_queue.empty():
            prio, _, plan = self._survey_queue.get()
            prio: int
            plan: FollowUpSurveyPlanner
            if plan.site_id == site_id:
                target_plan = plan
            else:
                new_queue.put(prio, plan)
        self._survey_queue: PriorityQueueWithFIFO = new_queue
        return prio, target_plan

    def requeue_survey_plan(
        self, prio: int, survey_plan: FollowUpSurveyPlanner
    ) -> None:
        self._survey_queue.put(
            priority=(prio, survey_plan.rate_at_site), item=survey_plan
        )

    def add_to_survey_queue(self, survey_plan: FollowUpSurveyPlanner) -> None:
        """Add the supplied site to the survey queue to surveyed

        Args:
            site (Site): The site to be added to the survey queue
        """
        self._survey_queue.put(
            (GenericSchedule.DEFAULT_SURVEY_PRIORITY, survey_plan.rate_at_site),
            survey_plan,
        )

    def add_unfinished_to_survey_queue(
        self, survey_plan: FollowUpSurveyPlanner
    ) -> None:
        """Add the supplied, partial surveyed site to queue

        Args:
            site (Site) : the Site to be added to the survey queue"""
        self._survey_queue.put(
            (
                GenericSchedule.UNFINISHED_SURVEY_HIGHEST_PRIORITY,
                survey_plan.rate_at_site,
            ),
            survey_plan,
        )

    def add_previous_queued_to_survey_queue(
        self, survey_plan: FollowUpSurveyPlanner
    ) -> None:
        """Add the supplied, unattended site back to queue

        Args:
            site (Site) : the Site to be added to the survey queue"""
        self._survey_queue.put(
            (GenericSchedule.QUEUED_SURVEY_PRIORITY, survey_plan.rate_at_site),
            survey_plan,
        )