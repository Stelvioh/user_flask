from repository.user_repository import UserRepository
from domain.user import User

class UserService:
    @staticmethod
    def add_user(user_dto):
        user = User(name=user_dto['name'], email=user_dto['email'])
        return UserRepository.add_user(user)

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()
