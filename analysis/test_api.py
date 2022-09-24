from pathlib import Path
from csv import DictReader

from api import (
    sort_by_field_ascending,
    filter_by_field,
    get_dict_of_value_counts_in_field,
)


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
