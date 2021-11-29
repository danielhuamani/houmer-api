from src.services import HoumerService
from src.exceptions import InvalidMaxDistanceVisit
import pytest

def test_service_complete_visit_success(create_houmer_a):
    service = HoumerService()
    instance = service.complete_visit(-12.102333, -77.023114, create_houmer_a)
    assert instance.latitude_end == None
    assert instance.longitude_end == None
    assert instance.speed is  None
    assert instance.distance is  None
    assert instance.spend_time is not  None
    assert instance.date_end is not  None


def test_service_complete_visit_invalid(create_houmer_a):
     with pytest.raises(InvalidMaxDistanceVisit) as e:
        service = HoumerService()
        service.complete_visit(-12.102832, -77.027824, create_houmer_a)
        assert e.message == "maximum distance not allowed"
 