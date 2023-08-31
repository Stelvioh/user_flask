from flask import Blueprint, request, jsonify
import service.user_service as service

class UserController:
    blueprint = Blueprint('users', __name__)

    @staticmethod
    @blueprint.route('/', methods=['GET'])
    def get_all_users():
        userDtoLists = service.UserService.get_all_users()
        return jsonify([user_dto.__dict__ for user_dto in userDtoLists])

    @staticmethod
    @blueprint.route('/', methods=['POST'])
    def add_user():
        user_data = request.get_json()
        userDto = service.UserService.add_user(user_data)
        return jsonify(userDto.__dict__), 201
