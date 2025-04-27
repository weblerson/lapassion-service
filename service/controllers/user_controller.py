from flask import views, request, jsonify, Blueprint

from services import UsersService
from repositories import UsersRepository


list_users_bp = Blueprint('list_users', __name__)


class ListUserController(views.MethodView):
    def __init__(self, users_service: UsersService):
        self.__users_service = users_service

    def get(self):
        users = self.__users_service.list()
        data = {
            'users': str(users.fetchall())
        }

        return jsonify(data), 200

    def post(self):
        name = request.json['name']

        self.__users_service.create(name)

        return jsonify(), 201


list_users_bp.add_url_rule(
    '/users/',
    view_func=ListUserController.as_view(
        'list_users',
        UsersService(UsersRepository()),
    )
)
