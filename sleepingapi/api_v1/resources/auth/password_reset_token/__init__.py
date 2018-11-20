# -*- coding: utf-8 -*-
"""
    Password Reset Token Resource
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Contains user password reset related resources to be accessed from
    this API. Normally used for handling cases where a user's password
    has been forgotten.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from http import HTTPStatus

from flask import current_app, request
from flask_restful import Resource
from itsdangerous import TimedJSONWebSignatureSerializer
from marshmallow import fields
from sendgrid import SendGridAPIClient
from werkzeug.exceptions import BadRequest, UnprocessableEntity

from sleepingapi.common.email import SendGridMailFactory
from sleepingapi.schema import ma

from ...user.controller import UserController
from .task import send_email


class PasswordResetTokenResource(Resource):
    """Serves as a resource for a password reset token."""

    class GetSchema(ma.Schema):
        """Serves as a schema for password reset GET requests."""

        email_address = fields.Email()

    def get(self):
        """Gets a password reset token.
        
        :raises BadRequest: Invalid or missing request body
        :raises UnprocessableEntity: Invalid request body content
        """

        if request.json is None:
            raise BadRequest("Missing JSON content.")

        # Check input validity.
        request_body, errors = self.GetSchema().load(request.json)
        if errors:
            raise UnprocessableEntity({
                    'errors': errors
                })

        # Get the user.
        user = UserController().get_by_email_address(
                request_body['email_address']
            )

        # Generate a password reset token.
        expires_in = current_app.config['PASSWORD_RESET_TOKEN_DURATION']
        password_reset_token = user.generate_password_reset_token(expires_in)
        print(request.json)

        # Send an email regarding the password reset.
        sg_api_client = SendGridAPIClient(
                apikey=current_app.config['SENDGRID_API_KEY']
            )
        mail = SendGridMailFactory().create_mail('', '', '', '')
        print(request.json)
        send_email(sg_api_client, mail)
        print(request.json)

        return {
            'password_reset_token': password_reset_token.decode('utf-8'),
            'expires_in': expires_in
        }, HTTPStatus.ACCEPTED
