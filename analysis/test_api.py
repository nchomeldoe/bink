from pathlib import Path
from csv import DictReader

from api import sort_by_field_ascending


proj_root = Path(__file__).parent.parent.resolve()
data_path = f"{proj_root}/data/test_data.csv"

with open(data_path) as csv_file:
    csv_reader = DictReader(csv_file, delimiter=",")
    data = list(csv_reader)


def test_sort_by_field_ascending():
    sorted_data = sort_by_field_ascending(data, "Dollars")
    assert sorted_data[0]["Name"] == "gav" and sorted_data[6]["Name"] == "trev"
