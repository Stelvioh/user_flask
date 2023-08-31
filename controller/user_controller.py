from flask import Blueprint, request, jsonify
from dto.user_dto import UserDTO

class UserController:
    blueprint = Blueprint('users', __name__)

    @staticmethod
    @blueprint.route('/', methods=['GET'])
    def get_all_users():
        from service.user_service import UserService
        users = UserService.get_all_users()
        user_dtos = [UserDTO.from_model(user) for user in users]
        return jsonify([user_dto.__dict__ for user_dto in user_dtos])

    @staticmethod
    @blueprint.route('/', methods=['POST'])
    def add_user():
        from service.user_service import UserService
        user_data = request.get_json()
        user = UserService.add_user(user_data)
        return jsonify(UserDTO.from_model(user).__dict__), 201
