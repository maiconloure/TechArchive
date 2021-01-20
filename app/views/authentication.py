from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from datetime import timedelta
from http import HTTPStatus

from app.services.user_services import create_user
from app.services.http import build_api_response
from app.models import User

bp_auth = Blueprint('auth', __name__, url_prefix='/')


@bp_auth.route('/login', methods=['POST'])
def login():

    email = request.json.get('email')
    password = request.json.get('password')

    getdata = User.query.all()

    for i in range(len(getdata)):
        if email == getdata[i].email:

            if password == getdata[i].password:
                access_token = create_access_token(
                    identity=getdata[i].id, expires_delta=timedelta(days=7))
                return {'token': access_token}

            return build_api_response(HTTPStatus.UNAUTHORIZED)

    return build_api_response(HTTPStatus.FORBIDDEN)
