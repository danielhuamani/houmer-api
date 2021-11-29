import pytest
from tests.factories.houmer import create_houmer
from uuid import uuid4
from src.utils import now_date
from datetime import timedelta

@pytest.fixture
def create_houmer_a():
    now = now_date()
    return create_houmer(id=str(uuid4()), houmer_id=1, date_start=now, latitude_start=-12.1023814, longitude_start=-77.0231919)

@pytest.mark.order(2)
@pytest.fixture
def create_houmer_b():
    print("create_houmer_b")
    now = now_date() - timedelta(days=2)
    return create_houmer(id=str(uuid4()), houmer_id=3, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964)

@pytest.mark.order(1)
@pytest.fixture
def create_houmer_b_2():
    print("create_houmer_b_2")
    now = now_date()
    return create_houmer(id=str(uuid4()), houmer_id=3, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964)

@pytest.fixture
def create_houmer_speed_1():
    now = now_date()
    return create_houmer(id=str(uuid4()), houmer_id=4, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964, speed=20)

@pytest.fixture
def create_houmer_speed_2():
    now = now_date()
    return create_houmer(id=str(uuid4()), houmer_id=4, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964, speed=10)

@pytest.fixture
def create_houmer_speed_null_3():
    now = now_date()
    return create_houmer(id=str(uuid4()), houmer_id=4, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964)

@pytest.fixture
def create_houmer_visit():
    now = now_date()
    now_late = now + timedelta(minutes=20)
    return create_houmer(id=str(uuid4()), houmer_id=4, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964, latitude_end=-12.1226755, longitude_end=-77.0566964, speed=20, distance=200, date_end=now_late, spend_time="02:20")


@pytest.fixture
def create_houmer_visit_completed():
    now = now_date()
    now_late = now + timedelta(minutes=20)
    return create_houmer(id=str(uuid4()), houmer_id=5, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964, latitude_end=-12.1226755, longitude_end=-77.0566964, speed=20, distance=200, date_end=now_late, spend_time="02:20")


@pytest.fixture
def create_houmer_visit_incomplement():
    now = now_date()
    now_late = now + timedelta(minutes=20)
    return create_houmer(id=str(uuid4()), houmer_id=5, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964)


@pytest.fixture
def create_houmer_visit_completed_2():
    now = now_date()
    now_late = now + timedelta(minutes=20)
    return create_houmer(id=str(uuid4()), houmer_id=6, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964, latitude_end=-12.1226755, longitude_end=-77.0566964, speed=10, distance=200, date_end=now_late, spend_time="04:20")

@pytest.fixture
def create_houmer_visit_completed_3():
    now = now_date()
    now_late = now + timedelta(minutes=20)
    return create_houmer(id=str(uuid4()), houmer_id=5, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964, latitude_end=-12.1226755, longitude_end=-77.0566964, speed=10, distance=200, date_end=now_late, spend_time="04:20")
