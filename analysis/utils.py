from datetime import datetime, date


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
