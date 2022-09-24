from datetime import date

from utils import string_to_date


def sort_by_field_ascending(df: list, field: str) -> list:
    """Sorts a dataframe based on a numerical field"""
    return sorted(df, key=lambda row: float(row[field]))


def filter_by_field(df: list, field: str, filter: str) -> list:
    """Filters dataframe to rows where field matches value"""
    return [row for row in df if row[field] == filter]


def get_dict_of_value_counts_in_field(df: list, field: str) -> list:
    """Returns a dict showing count of values in a field"""
    field = [row[field] for row in df]
    keys = set(field)
    dict = {}
    for key in keys:
        count = len([val for val in field if val == key])
        dict[key] = count
    return dict


def filter_date_field_within_dates(
    df: list, field: str, after: date, before: date
) -> list:
    """Filter dataset between two dates"""
    return [row for row in df if after <= string_to_date(row[field]) <= before]
