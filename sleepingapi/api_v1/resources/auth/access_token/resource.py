# -*- coding: utf-8 -*-
"""
    Access Token Resource
    ~~~~~~~~~~~~~~~~~~~~~

    Contains access token related resources to be accessed from this
    API.
"""
from http import HTTPStatus
from flask import current_app, g
from flask_restful import Resource

from ....auth import basic_auth


class AccessTokenResource(Resource):
    """Serves as a resource for an access token."""

    decorators = [
        basic_auth.login_required
    ]

    def get(self):
        """Gets an access token resource."""

        expires_in = current_app.config['ACCESS_TOKEN_DURATION']
        access_token = g.current_user.generate_auth_token(
            expires_in=expires_in)

        return {
            'access_token': access_token.decode('utf-8'),
            'expires_in': expires_in
        }, HTTPStatus.OK
