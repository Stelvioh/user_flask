from flask import abort, make_response, jsonify
from domain.user import User
from app import db
from sqlalchemy import exc

class UserRepository:

    @staticmethod
    def add_user(user):
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except exc.IntegrityError:
           abort(make_response( jsonify({ "message" : "Erro ao criar usuário"}),400))

    @staticmethod
    def get_all_users():
        return User.query.all()
