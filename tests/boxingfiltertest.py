import json
import pytest
import datetime
from app.models.boxingfilter import Filter

@pytest.fixture
def my_instance():
    return Filter()

@pytest.mark.parametrize("top, month, title, expected_result", [
    (None, None, None, "all_none"),
    ("not_an_int", "JAN", "TRUE", "invalid"),
    (10, "invalid_month", "TRUE", "invalid"),
    (10, "JAN", "invalid_title", "invalid"),
    (None, "JAN", "TRUE", "invalid"),
    (10, None, "TRUE", "invalid"),
    (10, "JAN", None, "invalid"),
    (10, "JAN", 10, "invalid"),
    (50, "JAN", "TRUE", "invalid"),
    (40, "JAN", "TRUE", "filter"),
    (30, "ANY", "ANY", "filter"),
    (30, "FEB", "FALSE", "filter"),
])
def test_check_valid(my_instance, top, month, title, expected_result):
    result = my_instance.check_valid(top, month, title)
    assert result == expected_result


# filter_fights
# get_fights
# get_fight_by_name


# get_today_date
@pytest.mark.parametrize("mock_date, expected_result", [
    (datetime.datetime(2022, 1, 1), "Jan 1"),
    (datetime.datetime(2022, 12, 31), "Dec 31"),
    (datetime.datetime(2022, 7, 25), "Jul 25"),
    (datetime.datetime(2022, 10, 5), "Oct 5"),
])
def test_get_today_date(my_instance, mock_date, expected_result):
    my_instance.get_today_date = lambda: mock_date.strftime("%b %-d")
    result = my_instance.get_today_date()
    assert result == expected_result


# get_fights_today
@pytest.mark.parametrize("fights, expected_fights, date", [
    ("fights.json", "result1.json", "Jan 31"),
    ("fights.json", "result2.json", "Mar 1"),
    ("fights.json", "result3.json", "Sep 15")
])
def test_get_fights_today(my_instance, fights, expected_fights, date):
    pass
