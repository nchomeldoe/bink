from pathlib import Path
from csv import DictReader

from api import (
    sort_by_field_ascending,
    filter_by_field,
    get_dict_of_value_counts_in_field,
    filter_date_field_within_dates,
)
from utils import string_to_date


proj_root = Path(__file__).parent.parent.resolve()
data_path = f"{proj_root}/data/test_data.csv"

with open(data_path) as csv_file:
    csv_reader = DictReader(csv_file, delimiter=",")
    data = list(csv_reader)


def test_sort_by_field_ascending():
    sorted_data = sort_by_field_ascending(data, "Dollars")
    assert sorted_data[0]["Name"] == "gav" and sorted_data[6]["Name"] == "trev"


def test_filter_by_field():
    filtered_data = filter_by_field(data, "Name", "dan")
    assert len(filtered_data) == 2


def test_get_dict_of_value_counts_in_field():
    dict = get_dict_of_value_counts_in_field(data, "Name")
    assert dict["dan"] == 2 and dict["josh"] == 1


def test_filter_date_field_within_dates_1():
    after = string_to_date("29 Jan 1971")
    before = string_to_date("29 Jan 1973")
    filtered_data = filter_date_field_within_dates(data, "DOB", after, before)
    assert filtered_data[0]["Name"] == "tom" and len(filtered_data) == 1


def test_filter_date_field_within_dates_2():
    after = string_to_date("16 Nov 1999")
    before = string_to_date("02 Aug 2001")
    filtered_data = filter_date_field_within_dates(data, "DOB", after, before)
    assert len(filtered_data) == 2
