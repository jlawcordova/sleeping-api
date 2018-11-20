# -*- coding: utf-8 -*-
"""
    User Resource
    ~~~~~~~~~~~~~

    Contains user related resources to be accessed from this API.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from http import HTTPStatus
from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest, UnprocessableEntity

from ...auth import basic_auth, token_auth
from .controller import UserController
from .schema import UserSchema


class UserResource(Resource):
    """Serves as a resource for User."""

    decorators = [
        token_auth.login_required
    ]

    def get(self, id=None):
        """Gets a User resource.

        :param id: User id, defaults to None
        :type id: 12-byte string
        :return: User json
        :rtype: werkzeug.Response,
                content-type='application/json', status_code=200
        """
        user = UserController().get(id)

        user = UserSchema().dump(user).data
        user = {
            'user': user
        }
        return user, HTTPStatus.OK

    def put(self, id=None):
        """Puts a User resource.

        :param id: not used, defaults to None
        :type id: 12-byte string, optional
        :return: created User json
        :rtype: werkzeug.Response,
                content-type='application/json', status_code=201
        """
        if request.json is None:
            raise BadRequest("Missing JSON content.")

        user = UserController().upsert(id, request.json)

        user = UserSchema().dump(user).data
        user = {
            'user': user
        }
        return user, HTTPStatus.OK

    def patch(self, id=None):
        """Patches a User resource.

        :param id: not used, defaults to None
        :type id: 12-byte string, optional
        :return: patched User json
        :rtype: werkzeug.Response,
                content-type='application/json', status_code=201
        """
        if request.json is None:
            raise BadRequest("Missing JSON content.")

        user = UserController().update_name(id, request.json)

        user = UserSchema().dump(user).data
        user = {
            'user': user
        }
        return user, HTTPStatus.OK


class UsersResource(Resource):
    """Serves as a resource for Foos."""

    @token_auth.login_required
    def get(self):
        """Gets all the User resource.

        :return: all User json
        :rtype: werkzeug.Response,
                content-type='application/json', status_code=200
        """
        users = UserController().get_all()

        users = UserSchema(many=True).dump(users).data
        users = {
            'users': users
        }
        return users, HTTPStatus.OK

    def post(self):
        """Posts a User resource.

        :return: created User json
        :rtype: werkzeug.Response,
                content-type='application/json', status_code=201
        """
        if request.json is None:
            raise BadRequest("Missing JSON content.")

        request_body, errors = UserSchema().load(request.json) # pylint: disable=W0612
        if errors:
            raise UnprocessableEntity({
                'errors': errors
            })

        user = UserController().insert(request.json)

        user = UserSchema().dump(user).data
        user = {
            'user': user
        }
        return user, HTTPStatus.CREATED
