from pathlib import Path
from csv import DictReader
import json

from api import (
    sort_by_field_ascending,
    filter_by_field,
    get_dict_of_value_counts_in_field,
    filter_date_field_within_dates,
)
from utils import string_to_date, read_csv_to_list_of_dicts, reformat_date_fields


proj_root = Path(__file__).parent.parent.resolve()
data_path = f"{proj_root}/data/mast_data.csv"
data = read_csv_to_list_of_dicts(data_path)


def question_one():
    print("\n\n   Q1 - cheapest five Current Rent")
    sorted_data = sort_by_field_ascending(data, "Current Rent")
    cheapest_five = sorted_data[:5]
    for i, val in enumerate(cheapest_five):
        print(i + 1)
        print(val)


def question_two():
    print("\n\n   2a - Lease years == 25...")
    filtered_data = filter_by_field(data, "Lease Years", "25")
    for i, val in enumerate(filtered_data):
        print(i + 1)
        print(val)
    print("\n   ...Q2b - and the sum of their rents")
    total_rent = sum([float(row['Current Rent']) for row in filtered_data])
    print(total_rent)


def question_three():
    print("\n\n   Q3 - Dict of tenant counts (unnormalised)")
    dict = get_dict_of_value_counts_in_field(data, "Tenant Name")
    pretty_dict = json.dumps(dict, sort_keys=True, indent=4)
    print(pretty_dict)


def question_four():
    print("\n\n   Q4 - Leases started between 01 Jun 1999 and 31 Aug 2007")
    after = string_to_date("01 Jun 1999")
    before = string_to_date("31 Aug 2007")
    date_restricted_data = filter_date_field_within_dates(
        data, "Lease Start Date", after, before
    )
    reformatted_data = reformat_date_fields(
        date_restricted_data, ["Lease Start Date", "Lease End Date"]
    )

    for i, val in enumerate(reformatted_data):
        print(i + 1)
        print(val)
