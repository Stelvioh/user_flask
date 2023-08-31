from repository.user_repository import UserRepository
from domain.user import User
from dto.user_dto import UserDTO

class UserService:

    @staticmethod
    def get_all_users():
         users =  UserRepository.get_all_users()
         return [UserDTO.from_model(user) for user in users]
        
    
    @staticmethod
    def add_user(user_dto):
        user = User(name=user_dto['name'], email=user_dto['email'])
        return UserDTO.from_model(UserRepository.add_user(user))
