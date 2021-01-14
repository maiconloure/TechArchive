from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.flask_models import User, db, UserSchema
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.user_services import serialize_user_list
import hashlib

bp_users = Blueprint('api_users', __name__, url_prefix='/users')


@bp_users.route('/')
def list_all():
    users = User.query.all()

    return {
        'data': serialize_user_list(users)
    }, HTTPStatus.OK


@bp_users.route('/', methods=['POST'])
def create():
    data = request.get_json()
    user = User(
        name=data["name"],
        description=data['description'],
        email=data['email'],
        password=hashlib.sha256(data['password'].encode('utf-8')).hexdigest(),
    )

    try:
        db.session.add(user)
        db.session.commit()
        return 'OK', HTTPStatus.CREATED

    except IntegrityError:
        return 'ERROR', HTTPStatus.BAD_REQUEST
