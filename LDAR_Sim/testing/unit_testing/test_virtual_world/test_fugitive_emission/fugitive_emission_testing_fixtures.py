from datetime import date
from typing import Tuple
import pytest

from virtual_world.fugitive_emission import FugitiveEmission


@pytest.fixture(name="mock_simple_fugitive_emission_for_activate_testing_1")
def mock_simple_fugitive_emission_for_activate_testing_1_fix() -> FugitiveEmission:
    return FugitiveEmission(1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), False, {}, 14, 200, 365)


@pytest.fixture(name="mock_simple_fugitive_emission_for_check_if_repaired_testing_1")
def mock_simple_fugitive_emission_for_check_if_repaired_testing_1_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), False, {}, 14, 200, 365
    )
    to_ret._days_since_tagged = 30
    to_ret._active_days = 60
    return to_ret


@pytest.fixture(name="mock_simple_fugitive_emission_for_check_if_repaired_testing_2")
def mock_simple_fugitive_emission_for_check_if_repaired_testing_2_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._days_since_tagged = 30
    to_ret._active_days = 60
    return to_ret, date(*[2018, 3, 2])


@pytest.fixture(name="mock_simple_emission_for_get_summary_dict")
def mock_simple_emission_for_get_summary_dict_1_fix() -> Tuple[FugitiveEmission, dict[str, int]]:
    return (
        FugitiveEmission(
            1,
            1,
            date(*[2018, 1, 1]),
            date(*[2017, 1, 1]),
            False,
            {"M_OGI1": 1, "M_AIR1": 1, "M_OGI2": 0, "M_AIR2": 0},
            14,
            200,
            365,
        ),
        {
            "Date Began": date(2018, 1, 1),
            "Days Active": 0,
            "Emissions ID": "0000000001",
            "Initially Detected By": None,
            "Status": "Inactive",
            "Tagged": False,
            "Tagged By": None,
            "Volume Emitted": 0.0,
            "Date Repaired": None,
        },
    )


@pytest.fixture(name="mock_simple_fugitive_emission_for_natural_repair_testing_1")
def mock_simple_fugitive_emission_for_natural_repair_testing_1_fix() -> (
    Tuple[FugitiveEmission, date]
):
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._days_since_tagged = 30
    to_ret._active_days = 60
    return to_ret, date(*[2018, 3, 2])


@pytest.fixture(name="mock_simple_fugitive_emission_for_tag_leak_testing_1")
def mock_simple_fugitive_emission_for_tag_leak_testing_1_fix() -> (
    Tuple[
        FugitiveEmission,
        Tuple[float, date, int, str, str, int],
    ]
):
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._active_days = 60
    return to_ret, (1, date(*[2017, 6, 1]), 1, "test", "test", 1)


@pytest.fixture(name="mock_simple_fugitive_emission_for_tag_leak_testing_already_tagged")
def mock_simple_fugitive_emission_for_tag_leak_testing_already_tagged_fix() -> (
    Tuple[
        FugitiveEmission,
        Tuple[float, date, int, str, str, int],
    ]
):
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._active_days = 60
    to_ret._tagged = True
    return to_ret, (1.0, date(*[2017, 6, 1]), 1, "test", "test", 1)


@pytest.fixture(name="mock_simple_fugitive_emission_for_tagged_today_testing_just_tagged")
def mock_simple_fugitive_emission_for_tagged_today_testing_just_tagged_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._days_since_tagged = 0
    to_ret._tagged = True
    to_ret._tagged_by_company = "Test"
    return to_ret


@pytest.fixture(name="mock_simple_fugitive_emission_for_tagged_today_testing_not_tagged")
def mock_simple_fugitive_emission_for_tagged_today_testing_not_tagged_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._tagged = False
    return to_ret


@pytest.fixture(name="mock_simple_fugitive_emission_for_tagged_today_testing_tagged_previously")
def mock_simple_fugitive_emission_for_tagged_today_testing_tagged_previously_fix() -> (
    FugitiveEmission
):
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._days_since_tagged = 60
    to_ret._tagged = True
    to_ret._tagged_by_company = "Test"
    return to_ret


@pytest.fixture(name="mock_simple_fugitive_emission_for_tagged_today_testing_tagged_by_natural")
def mock_simple_fugitive_emission_for_tagged_today_testing_tagged_by_natural_fix() -> (
    FugitiveEmission
):
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._days_since_tagged = 0
    to_ret._tagged = True
    to_ret._tagged_by_company = "natural"
    return to_ret


@pytest.fixture(name="mock_fugitive_emission_for_update_detection_records_no_prior_detection")
def mock_fugitive_emission_for_update_detection_records_no_prior_detection_fix() -> (
    FugitiveEmission
):
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    return to_ret


@pytest.fixture(name="mock_fugitive_emission_for_update_detection_records_w_prior_detection")
def mock_fugitive_emission_for_update_detection_records_w_prior_detection_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._init_detect_by = "test"
    to_ret._init_detect_date = date(*[2018, 1, 2])
    return to_ret


@pytest.fixture(name="mock_fugitive_emission_for_update_ready_for_nat_repair")
def mock_fugitive_emission_for_update_ready_for_nat_repair_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._active_days = 364
    to_ret._status = "Active"
    return to_ret


@pytest.fixture(name="mock_fugitive_emission_for_update_no_status_change")
def mock_fugitive_emission_for_update_no_status_change_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._active_days = 60
    to_ret._status = "Active"
    return to_ret


@pytest.fixture(name="mock_fugitive_emission_for_update_no_status_change_emission_tagged")
def mock_fugitive_emission_for_update_no_status_change_emission_tagged_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._active_days = 60
    to_ret._status = "Active"
    to_ret._tagged = True
    to_ret._days_since_tagged = 1
    return to_ret


@pytest.fixture(name="mock_fugitive_emission_for_update_newly_repaired")
def mock_fugitive_emission_for_update_newly_repaired_fix() -> FugitiveEmission:
    to_ret = FugitiveEmission(
        1, 1, date(*[2018, 1, 1]), date(*[2017, 1, 1]), True, {}, 14, 200, 365
    )
    to_ret._active_days = 60
    to_ret._status = "Active"
    to_ret._tagged = True
    to_ret._days_since_tagged = 13
    return to_ret