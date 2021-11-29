from src.utils import now_date
from src.db.models import HoumerModel
from src.serializers import HoumerSerializer
import json

def test_api_visit_status_200(
    client, 
    create_houmer_visit_completed, 
    create_houmer_visit_incomplement, 
    create_houmer_visit_completed_2):
    now = now_date().strftime("%Y-%m-%d")
    response = client.get(f'/houmer/5/{now}/visit')
    data = json.loads(response.data)
    for x in HoumerModel.scan():
        print(x.id)
    assert len(data) == 2
    assert response.status_code == 200



def test_api_visit_empty(
    client, 
    create_houmer_visit_completed, 
    create_houmer_visit_incomplement, 
    create_houmer_visit_completed_2):
    now = now_date().strftime("%Y-%m-%d")
    response = client.get(f'/houmer/8/{now}/visit')
    data = json.loads(response.data)
    assert len(data) == 0
    assert response.status_code == 200

def test_api_speed_with_parameter(
    client, 
    create_houmer_visit_completed, 
    create_houmer_visit_incomplement, 
    create_houmer_visit_completed_3):
    now = now_date().strftime("%Y-%m-%d")
    response = client.get(f'/houmer/5/{now}/speed?speed=12')
    data = json.loads(response.data)
    assert len(data) == 1
    assert response.status_code == 200

def test_api_speed_without_parameter(
    client, 
    create_houmer_visit_completed, 
    create_houmer_visit_incomplement, 
    create_houmer_visit_completed_3):
    now = now_date().strftime("%Y-%m-%d")
    response = client.get(f'/houmer/5/{now}/speed')
    data = json.loads(response.data)
    assert len(data) == 2
    assert response.status_code == 200

def test_api_first_visit_property(
    client):
    response = client.post(f'/houmer/10/coordinates', data=json.dumps({
        'longitude': -12.103194,
        'latitude': -77.029797
        }),
        content_type='application/json'
    )
    houmers = HoumerModel.scan()
    houmer_serializer = HoumerSerializer()
    data = houmer_serializer.visit(houmers)
    item = data[0]
    assert len(data) == 1
    assert response.status_code == 201
    assert item['longitude'] == -12.103194
    assert item['latitude'] == -77.029797


def test_api_completed_visit(
    client, create_houmer_visit_completed, create_houmer_visit_completed_3):
    now = now_date().strftime("%Y-%m-%d")
    response = client.post(f'/houmer/5/coordinates', data=json.dumps({
        'longitude': -12.103194,
        'latitude': -77.029797
        }),
        content_type='application/json'
    )
    houmers = HoumerModel.query(5, limit=3, scan_index_forward=False)
    houmer_serializer = HoumerSerializer()
    data = houmer_serializer.visit(houmers)
    item = data[0]
    assert len(data) == 3
    assert response.status_code == 201
    assert item['latitude'] == -77.029797
    assert item['longitude'] == -12.103194


def test_api_init_other_visit_after_completed_visit(
    client, create_houmer_visit_incomplement_2):
    response = client.post(f'/houmer/5/coordinates', data=json.dumps({
        'longitude': -12.1033048,
        'latitude': -77.0301591
        }),
        content_type='application/json'
    )
    houmers = HoumerModel.query(5, limit=3, scan_index_forward=False)
    houmer_serializer = HoumerSerializer()
    data = houmer_serializer.visit(houmers)
    item = data[0]
    assert len(data) == 2
    assert response.status_code == 201
    assert item['latitude'] == -77.0301591
    assert item['longitude'] == -12.1033048