from flask_restx import Resource, Namespace

from app import models
from app.database import db
from app.schemas.movies import MovieSchema
from flask import request

movies_ns = Namespace('movies')


@movies_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()

        if movie is None:
            return {}, 404

        return MovieSchema().dump(movie), 200

    def put(self, movie_id):
        db.session.query(models.Movie).filter(models.Movie.id == movie_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, movie_id):
        db.session.query(models.Movie).filter(models.Movie.id == movie_id).delete()
        db.session.commit()

        return None, 200


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year_id = request.args.get("year")
        movies = db.session.query(models.Movie)
        if director_id is not None:
            movies = movies.filter(models.Movie.director_id == director_id)
        if genre_id is not None:
            movies = movies.filter(models.Movie.genre_id == genre_id)
        if year_id is not None:
            movies = movies.filter(models.Movie.year == year_id)
        all_movies = movies.all()
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    def post(self):
        movie = MovieSchema().load(request.json)
        db.session.add(models.Movie(**movie))
        db.session.commit()

        return None, 201
