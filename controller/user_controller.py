from flask_classful import FlaskView, route
from service.user_service import UserService
from flask import request, jsonify

class UserController(FlaskView):

    @route('/', methods=['GET'])
    def get_all_users(self):
        userDtoLists = UserService.get_all_users()
        return jsonify([user_dto.__dict__ for user_dto in userDtoLists])

    @route('/', methods=['POST'])
    def add_user(self):
        user_data = request.get_json()
        userDto = UserService.add_user(user_data)
        return jsonify(userDto.__dict__), 201