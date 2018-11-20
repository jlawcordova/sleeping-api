"""
    API v1 Auth
    ~~~~~~~~~~~

    The main API v1 auth module.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from flask import g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.exceptions import Unauthorized

from .resources.user.model import User
from .resources.user.controller import UserController

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(email_address, password):
    user = UserController().get_by_email_address(email_address)
    if not user:
        return False

    g.current_user = user
    return user.verify_password(password)

@token_auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)

    return (user is not None)

@basic_auth.error_handler
@token_auth.error_handler
def auth_error():
    raise Unauthorized({'errors': {
                'name': 'unauthorized',
                'description': "The server could not verify that you are \
authorized to access the URL requested. You either supplied the wrong \
credentials (e.g. a bad password), or your browser doesn't understand how to \
supply the credentials required."
            }
        })
