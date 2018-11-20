# -*- coding: utf-8 -*-
"""
    SleepingAPI API v1 Blueprint
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The main SleepingAPI blueprint module.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from flask import Blueprint

from .api import api

from .resources.user import UserResource, UsersResource

from .resources.auth.access_token import AccessTokenResource
from .resources.auth.password_reset_token import PasswordResetTokenResource

bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Apply the RESTFul extension.
api.init_app(bp)

# Add the User resources.
api.add_resource(UserResource, '/user/<string:id>')
api.add_resource(UsersResource, '/user', '/user/')

# Add the Auth resources.
api.add_resource(AccessTokenResource, '/auth/access-token')
api.add_resource(PasswordResetTokenResource, '/auth/password-reset-token')
