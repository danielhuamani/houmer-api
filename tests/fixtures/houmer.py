import pytest
from tests.factories.houmer import create_houmer
from uuid import uuid4
from src.utils import now_date
from datetime import timedelta

@pytest.fixture
def create_houmer_a():
    return create_houmer(id=str(uuid4()), houmer_id=1, date_start=now_date(), latitude_start=-12.1026755, longitude_start=-77.0266964)

@pytest.mark.order(1)
@pytest.fixture
def create_houmer_b():
    now = now_date() - timedelta(days=2)
    return create_houmer(id=str(uuid4()), houmer_id=3, date_start=now, latitude_start=-12.1026755, longitude_start=-77.0266964)

@pytest.mark.order(2)
@pytest.fixture
def create_houmer_b_2():
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