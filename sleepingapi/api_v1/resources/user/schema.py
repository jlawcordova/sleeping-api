# -*- coding: utf-8 -*-
"""
    User Schema
    ~~~~~~~~~~~~~~~~

    Contains schemas for user related models.

    :copyright: (c) YYYY by John Doe.
    :license: MIT, see LICENSE for more details.
"""
# pylint: disable=E1101
from marshmallow import fields, validate
from marshmallow_mongoengine import ModelSchema

from sleepingapi.schema import ma

from .model import User


class UserSchema(ModelSchema):
    """Serves as a schema for user."""

    class Meta:
        """Meta schema for user."""

        model = User
        load_only = [
            'password'
        ]
        exclude = [
            'password_hash'
        ]

    password = fields.String(required=True, validate=[validate.Length(min=8)])
    url = ma.AbsoluteURLFor('api_v1.userresource', id='<id>')
