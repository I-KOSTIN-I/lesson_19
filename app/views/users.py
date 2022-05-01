from flask_restx import Resource, Namespace

from app import models
from app.database import db
from app.schemas.users import UserSchema
from flask import request

users_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@users_ns.route('/<int:user_id>')
class UsersView(Resource):
    def get(self, user_id):
        user = db.session.query(models.User).filter(models.User.id == user_id).first()

        if user is None:
            return {}, 404

        return user_schema.dump(user), 200

    def put(self, user_id):
        db.session.query(models.User).filter(models.User.id == user_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, user_id):
        db.session.query(models.User).filter(models.User.id == user_id).delete()
        db.session.commit()

        return None, 200


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = db.session.query(models.User).all()

        return users_schema.dump(users), 200

    def post(self):
        user = user_schema.load(request.json)
        db.session.add(models.User(**user))
        db.session.commit()

        return None, 201
