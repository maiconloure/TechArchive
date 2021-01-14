from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.flask_models import User, db, UserSchema
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from app.services.user_services import serialize_user_list, serialize_user
from app.services.http import build_api_response
import hashlib
from datetime import datetime
from pytz import timezone

fuso_horario = timezone('America/Sao_Paulo')
bp_users = Blueprint('api_users', __name__)


@bp_users.route('/users')
def list_all():
    users = User.query.all()

    return {
        'data': serialize_user_list(users)
    }, HTTPStatus.OK


@bp_users.route('/user/<user_id>')
def get_user(user_id):
    if User.query.filter_by(id=user_id).first() is not None:
        user = User.query.filter_by(id=user_id).first()
    else:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return {
        'data': serialize_user(user)
    }, HTTPStatus.OK


@bp_users.route('/user', methods=['POST'])
def create():
    data = request.get_json()
    user = User(
        name=data["name"],
        description=data['description'],
        email=data['email'],
        password=hashlib.sha256(data['password'].encode('utf-8')).hexdigest(),
        create_at=datetime.now(
        ).astimezone(fuso_horario).strftime('%d/%m/%Y %H:%M:%S'),
    )

    # Para descriptografar a senha, basta criptografar a senha de entrada da tela de login
    # e comparar com a senha criptografada no banco de dados, os hashs deverão ser iguais.

    try:
        db.session.add(user)
        db.session.commit()
        return build_api_response(HTTPStatus.CREATED)

    except IntegrityError:
        return build_api_response(HTTPStatus.BAD_REQUEST)


@bp_users.route('/user/<user_id>', methods=['PATCH'])
def update(user_id):

    if User.query.filter_by(id=user_id).first() is not None:
        data = request.get_json()
        user = User.query.get(user_id)

        user.name = data['name'] if data.get(
            'name') else user.name

        user.description = data['description'] if data.get(
            'description') else user.description

        user.email = data['email'] if data.get(
            'email') else user.email

        user.password = hashlib.sha256(data['password'].encode('utf-8')).hexdigest() if data.get(
            'password') else user.password

        user.user_type = data['user_type'] if data.get(
            'user_type') else user.user_type

        db.session.commit()

    else:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return build_api_response(HTTPStatus.OK)


@bp_users.route('/user/<user_id>', methods=['DELETE'])
def delete(user_id):
    if User.query.filter_by(id=user_id).first() is not None:
        user = User.query.filter_by(id=user_id).delete()
        db.session.commit()

    else:
        return build_api_response(HTTPStatus.NOT_FOUND)

    return build_api_response(HTTPStatus.OK)
