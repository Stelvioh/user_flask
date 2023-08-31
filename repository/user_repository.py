from domain.user import User
from app import db

class UserRepository:

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()
