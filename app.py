from flask import Flask
from domain.user import User
from database import db
from config import Config
from controller.user_controller import UserController


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    app.register_blueprint(UserController.blueprint)

    with app.app_context():
        db.create_all()    

    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
