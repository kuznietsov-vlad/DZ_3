from datetime import datetime, date


def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        print("Please write a correct date format: YYYY-MM-DD")
        return None

def get_days_from_today(date):
    date_obj = string_to_date(date)
    if date_obj is None:
        return None

    today = datetime.today().date()
    difference = (today - date_obj).days
    return difference

vlados='2020-10-09'
print(get_days_from_today(vlados))
