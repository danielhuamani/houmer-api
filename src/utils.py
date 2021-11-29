from datetime import date, datetime, timezone, timedelta
from time import strftime, gmtime

def now_date():
    return datetime.now(timezone.utc)

def seconds_to_str(seconds):
    return strftime("%H:%M", gmtime(seconds))

def date_to_datetime(d:date):
    return datetime(d.year, d.month, d.day)

def range_datetime(d):
    date_start = d.replace(tzinfo=timezone.utc, hour=0, minute=0, second=0, microsecond=0)
    date_end = d + timedelta(hours=24)
    return date_start, date_end

def convert_seconds_to_hours(seconds):
    return seconds / 3600.00

def convert_km_to_mt2(km):
    return km * 1000