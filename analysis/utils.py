from datetime import datetime, date
from csv import DictReader
from typing import Iterable


def read_csv_to_list_of_dicts(csv_path: str) -> list:
    with open(csv_path) as csv_file:
        csv_reader = DictReader(csv_file, delimiter=",")
        return list(csv_reader)


def string_to_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%d %b %Y").date()


def date_to_string(date: date) -> str:
    return datetime.strftime(date, "%d/%m/%Y")


def reformat_date_strings(date_str: str) -> str:
    date_obj = string_to_date(date_str)
    return date_to_string(date_obj)


def reformat_date_fields(df: list, fields: Iterable[str]) -> list:
    """Reformat date fields from provided to requested formats"""
    for field in fields:
        for row in df:
            row[field] = reformat_date_strings(row[field])
    return df


if __name__ == "__main__":
    string_date = "28 Jul 2018"
    dt = string_to_date(string_date)
    print("string to date,", dt, " ,type,", type(dt))
    str = date_to_string(dt)
    print("date to string,", str, " ,type,", type(str))
    new_format = reformat_date_strings(string_date)
    print("new format,", new_format, " ,type,", type(new_format))
