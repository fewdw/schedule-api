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
    (50, "JAN", "TRUE", "filter"),
    (50, "ANY", "ANY", "filter"),
    (50, "FEB", "FALSE", "filter"),
])
def test_check_valid(my_instance, top, month, title, expected_result):
    # Act
    result = my_instance.check_valid(top, month, title)
    # Assert
    assert result == expected_result


# tests to write....
# filter_fights
# get_fights
# get_fight_by_name
# get_today_date
# get_fights_today
# pytest -v tests/boxingfiltertest.py
