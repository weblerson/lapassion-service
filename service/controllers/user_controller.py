from flask import views, request, jsonify, Blueprint
from http import HTTPStatus

from services import UsersService
from repositories import UsersRepository


list_users_bp = Blueprint('list_users', __name__)


class ListUserController(views.MethodView):
    def __init__(self, users_service: UsersService):
        self.__users_service = users_service

    def get(self):
        list_users = self.__users_service.list()

        return jsonify(list_users.model_dump()), HTTPStatus.OK

    def post(self):
        name = request.json['name']
        user = self.__users_service.create(name)

        return jsonify(user.model_dump()), HTTPStatus.CREATED


list_users_bp.add_url_rule(
    '/users/',
    view_func=ListUserController.as_view(
        'list_users',
        UsersService(UsersRepository()),
    )
)
