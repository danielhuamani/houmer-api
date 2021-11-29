from datetime import date, datetime, timezone, timedelta
from time import strftime, gmtime
from geopy.distance import geodesic as GD

def now_date():
    now = datetime.now()
    return now

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

def convert_datetime_to_timestamp(now):
    timestamp = datetime.timestamp(now)
    return timestamp

def convert_timestamp_to_datetime(timestamp):
    now = datetime.fromtimestamp(timestamp)
    return now

def calculate_distance_km(point_start, point_end):
    if None in point_start and None in point_end:
        return None
    distance = GD(point_start, point_end).km
    return distance