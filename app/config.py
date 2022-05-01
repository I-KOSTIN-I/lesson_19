class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
