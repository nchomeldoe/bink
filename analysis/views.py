from pathlib import Path
from csv import DictReader

from api import sort_by_field_ascending


proj_root = Path(__file__).parent.parent.resolve()
data_path = f"{proj_root}/data/mast_data.csv"

with open(data_path) as csv_file:
    csv_reader = DictReader(csv_file, delimiter=",")
    data = list(csv_reader)


def question_one():
    sorted = sort_by_field_ascending(data, "Current Rent")
    cheapest_five = sorted[:5]
    for i, val in enumerate(cheapest_five):
        print(i + 1)
        print(val)
