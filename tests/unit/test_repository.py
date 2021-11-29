import os
import pytest
from datetime import timedelta
from src.utils import now_date, date_to_datetime, timezone, range_datetime
from src.db.models import HoumerModel
from src.repositories import HoumerRepository
from uuid import uuid4

def test_repository_last_by_houmer_none():
    print("test", os.environ.get('TABLE_HOUMER'))
    repository = HoumerRepository()
    houmer = repository.get_last_by_houmer(id=200)
    assert houmer == None


def test_repository_last_by_houmer_exists(create_houmer_b_2, create_houmer_b):
    repository = HoumerRepository()
    houmer = repository.get_last_by_houmer(id=3)
    assert houmer.id == create_houmer_b.id


def test_repository_get_by_range_date(create_houmer_b_2, create_houmer_b):
    now = now_date()
    date_start = date_to_datetime(now.date())
    date_start = date_start.replace(tzinfo=timezone.utc, hour=0, minute=0, second=0, microsecond=0)
    date_end = date_start + timedelta(hours=24)
    repository = HoumerRepository()
    houmers = repository.get_by_range_date(houmer_id=3, date_start=date_start, date_end=date_end)
    total_ids = []
    for x in houmers:
        total_ids.append(x.id)
    assert create_houmer_b_2.id in total_ids


def test_repository_get_by_range_date(create_houmer_b_2, create_houmer_b):
    now = now_date()
    date_start = date_to_datetime(now.date())
    date_start, date_end = range_datetime(date_start)
    repository = HoumerRepository()
    houmers = repository.get_by_range_date(houmer_id=3, date_start=date_start, date_end=date_end)
    total_ids = []
    for x in houmers:
        total_ids.append(x.id)
    assert create_houmer_b_2.id in total_ids


def test_repository_get_by_range_date_with_speed(create_houmer_b_2, create_houmer_b, create_houmer_speed_1, create_houmer_speed_2, create_houmer_speed_null_3):
    now = now_date()
    date_start = date_to_datetime(now.date())
    date_start, date_end = range_datetime(date_start)
    repository = HoumerRepository()
    houmers = repository.get_by_range_date_with_speed(houmer_id=4, date_start=date_start, date_end=date_end, speed=11)
    total_ids = []
    for x in houmers:
        total_ids.append(x.id)
    assert create_houmer_speed_1.id in total_ids
    assert len(total_ids) == 1

def test_repository_update(create_houmer_b_2):
    repository = HoumerRepository()
    repository.update(create_houmer_b_2, {"houmer_id": 5})
    houmers = HoumerModel.query(create_houmer_b_2.id)
    total_houmer_ids = []
    for x in houmers:
        total_houmer_ids.append(x.houmer_id)
    assert len(total_houmer_ids) == 1
    assert total_houmer_ids[0] == 5



def test_repository_create():
    id = str(uuid4())
    repository = HoumerRepository()
    instance = repository.create(
        {"houmer_id": 5, "id": id, "longitude_start": 20, "latitude_start": 30}
    )
    assert instance.id == id
    assert instance.houmer_id == 5
    assert instance.longitude_start == 20
    assert instance.latitude_start == 30