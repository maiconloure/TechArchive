from flask import Flask
from app.models.flask_models import db, mg, ma
from app.views.user import bp_users
from app.views.news import bp_news
from environs import Env


def create_app():
    env = Env()
    env.read_env()

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env.bool(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = env.str('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(bp_users)
    app.register_blueprint(bp_news)
    return app
