from datetime import datetime, date
from csv import DictReader


def read_csv_to_list_of_dicts(csv_path: str) -> list:
    with open(csv_path) as csv_file:
        csv_reader = DictReader(csv_file, delimiter=",")
        return list(csv_reader)


def string_to_date(time_str: str) -> date:
    return datetime.strptime(time_str, "%d %b %Y").date()


def date_to_string(date: date) -> str:
    return datetime.strftime(date, "%d/%m/%Y")


if __name__ == "__main__":
    string_date = "28 Jan 2018"
    dt = string_to_date(string_date)
    print("string to date,", dt, " ,type,", type(dt))
    str = date_to_string(dt)
    print("date to string,", str, " ,type,", type(str))
