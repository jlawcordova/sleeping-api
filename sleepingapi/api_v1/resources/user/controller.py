# -*- coding: utf-8 -*-
"""
    User Controller
    ~~~~~~~~~~~~~~~~

    Contains controllers for user related models.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
# pylint: disable=E1101
from sleepingapi.database import db

from .model import User
from .schema import UserSchema


class UserController(object):
    """Serves as a controller for user."""

    def get(self, id):
        with db.QueryContext():
            user = User.objects(id=id).first_or_404()

        return user

    def get_by_email_address(self, email_address):
        with db.QueryContext():
            user = User.objects(email_address=email_address) \
                .first_or_404()

        return user

    def get_all(self):
        with db.QueryContext():
            users = User.objects.all()

        return users

    def insert(self, user):
        # Don't allow ID on save.
        user.pop('id', None)

        password = user.pop('password', None)
        with db.QueryContext():
            user = User(**user)
            user.password = password
            user.save()

        return user

    def upsert(self, id, user):
        user['id'] = id

        with db.QueryContext():
            user = User(**user).save()

        return user

    def update_name(self, id, user):
        with db.QueryContext():
            user = User.objects(id=id) \
                .update(upsert=True,
                        set__given_name=user.get('given_name', None),
                        set__family_name=user.get('family_name', None))

        user = User.objects(id=id).first()

        return user
