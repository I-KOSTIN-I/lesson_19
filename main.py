from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.models import User
from app.views.directors import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns
from app.views.users import users_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="oleg", password="P@ssw0rd", role="admin")

        with db.session.begin():
            db.session.add_all([u1, u2, u3])


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(users_ns)
    #create_data(app, db)


app = create_app(Config())

if __name__ == '__main__':
    app.run(debug=True)
