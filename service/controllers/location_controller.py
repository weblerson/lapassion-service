from http import HTTPStatus
from flask import views, jsonify, request, Blueprint

from services import LocationService
from repositories import LocationRepository


list_location_bp = Blueprint('list_location', __name__)


class ListLocationController(views.MethodView):
    def __init__(self, location_service: LocationService):
        self.__location_service = location_service

    def get(self):
        results = self.__location_service.list()

        return jsonify(results.model_dump()), HTTPStatus.OK

    def post(self):
        # create validators
        # beta
        # blue pill
        lat = request.json['lat']
        lon = request.json['lon']
        klass = request.json['class']
        user_id = request.json['user_id']

        result = self.__location_service.create(
            lat, lon, klass, user_id
        )

        return jsonify(result.model_dump()), HTTPStatus.CREATED


list_location_bp.add_url_rule(
    '/locations/',
    view_func=ListLocationController.as_view(
        'list_locations',
        LocationService(LocationRepository())
    )
)
