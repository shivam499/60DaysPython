from datetime import date

def get_date_with_weekday_name():
    today = date.today()
    return today.strftime("%Y-%m-%d (%A)")

print(get_date_with_weekday_name())