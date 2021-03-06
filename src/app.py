from flask import Flask, request, jsonify
from marshmallow import ValidationError
from src.services import HoumerService
from src.validations import CoordinatesValidateSchema, ISODateConverter
from src.exceptions import InvalidMaxDistanceVisit
from src.serializers import HoumerSerializer
app = Flask(__name__)
app.url_map.converters['iso_date'] = ISODateConverter


@app.route("/houmer/<int:houmer_id>/coordinates", methods=['POST'])
def coordinates(houmer_id):
    request_data = request.get_json()
    service = HoumerService()
    serializer = HoumerSerializer()
    print(request_data, "reques", houmer_id, "houmer_id")
    try:
        result = CoordinatesValidateSchema().load(request_data)
        houmer = service.get_last_by_houmer(houmer_id=houmer_id)
        if houmer is not None:
            latitude = result.get('latitude')
            longitude = result.get('longitude')
            try:
                instance = service.complete_visit(latitude, longitude, houmer)
                return jsonify(serializer.coordinates(instance)), 200
            except InvalidMaxDistanceVisit as err:
                instance = service.create_or_update(houmer_id=houmer_id, latitude=result.get("latitude"), longitude=result.get("longitude"))
        else:
            instance = service.create(houmer_id=houmer_id, latitude_start=result.get("latitude"), longitude_start=result.get("longitude"))
        return jsonify(serializer.coordinates(instance)), 201
    except ValidationError as err:
        return jsonify(err), 403


@app.route("/houmer/<int:houmer_id>/<iso_date:selected_date>/visit", methods=['GET'])
def visit(houmer_id, selected_date):
    service = HoumerService()
    houmers = service.get_by_date(houmer_id=houmer_id, selected_date=selected_date)
    serializer = HoumerSerializer()
    return jsonify(serializer.visit(houmers)), 200


@app.route("/houmer/<int:houmer_id>/<iso_date:selected_date>/speed", methods=['GET'])
def speed(houmer_id, selected_date):
    speed = request.args.get('speed', 0, type=float)
    service = HoumerService()
    houmers = service.get_by_date_with_speed(
        houmer_id=houmer_id, selected_date=selected_date, speed=speed)
    serializer = HoumerSerializer()
    return jsonify(serializer.speed(houmers)), 200

if __name__ == "__main__":
    app.run()