from datetime import datetime
from src.db.models import HoumerModel
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute, UnicodeAttribute
from src.db.connection import Connection
import pytest

@pytest.fixture(autouse=True)
def set_config():
    HoumerModel.delete_table()
    if not HoumerModel.exists():
        HoumerModel.create_table(read_capacity_units=2, write_capacity_units=2, wait=True)
