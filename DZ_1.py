from datetime import datetime, date


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def calculation(date):
    today= datetime.today().date()
    difference= (today - string_to_date(date)).days
    message = f'from {date} to {today} - {difference} days'
    return message

vlados='2024.08.07'
prepared_vlados= string_to_date(vlados)
print(calculation(vlados))