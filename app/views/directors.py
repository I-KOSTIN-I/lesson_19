from flask_restx import Resource, Namespace
from app import models
from app.database import db
from app.schemas.directors import DirectorSchema
from flask import request

directors_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(models.Director).all()

        return directors_schema.dump(directors), 200

    def post(self):
        director = director_schema.load(request.json)
        db.session.add(models.Director(**director))
        db.session.commit()

        return None, 201


@directors_ns.route('/<int:director_id>')
class DirectorsView(Resource):
    def get(self, director_id):
        director = db.session.query(models.Director).filter(models.Director.id == director_id).first()

        if director is None:
            return {}, 404

        return director_schema.dump(director), 200

    def put(self, director_id):
        db.session.query(models.Director).filter(models.Director.id == director_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, director_id):
        db.session.query(models.Director).filter(models.Director.id == director_id).delete()
        db.session.commit()

        return None, 200
