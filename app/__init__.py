from flask import Flask
from flask_migrate import Migrate
from environs import Env

from app.configs import config_db
from app.views import config_views
from app.schema import config_serializer

def create_app(config='production'):
    env = Env()
    env.read_env()

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    config_db(app)
    config_serializer(app)
    Migrate(app)

    config_views(app)

    return app
