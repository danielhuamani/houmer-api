from datetime import date, datetime, timezone, timedelta
from time import strftime, gmtime

def now_date():
    return datetime.now(timezone.utc)

def seconds_to_str(seconds):
    return strftime("%H:%M", gmtime(seconds))

def date_to_datetime(d):
    return datetime(d.year, d.month, d.day)
