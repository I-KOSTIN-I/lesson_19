from flask_restx import Namespace, Resource


auth = Namespace('auth')


class AuthView(Resource):
    def post(self):
        pass
