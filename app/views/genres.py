from flask import request
from flask_restx import Resource, Namespace
from app.database import db
from app import models
from app.schemas.genres import GenreSchema

genres_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = db.session.query(models.Genre).all()

        return genres_schema.dump(genres), 200

    def post(self):
        genre = genre_schema.load(request.json)
        db.session.add(models.Genre(**genre))
        db.session.commit()

        return None, 201


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = db.session.query(models.Genre).filter(models.Genre.id == genre_id).first()

        if genre is None:
            return {}, 404

        return genre_schema.dump(genre), 200

    def put(self, genre_id):
        db.session.query(models.Genre).filter(models.Genre.id == genre_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, genre_id):
        db.session.query(models.Genre).filter(models.Genre.id == genre_id).delete()
        db.session.commit()

        return None, 200
