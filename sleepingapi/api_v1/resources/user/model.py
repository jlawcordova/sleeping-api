# -*- coding: utf-8 -*-
"""
    User Model
    ~~~~~~~~~~

    Contains user related models.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
# pylint: disable=E1101
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer
from werkzeug.security import check_password_hash, generate_password_hash

from sleepingapi.database import db


class User(db.Document):
    """Serves as a model for user."""

    given_name = db.StringField(required=True, nullable=False)
    family_name = db.StringField(required=True, nullable=False)
    email_address = db.EmailField(required=True, unique=True, nullable=False)
    password_hash = db.StringField(required=True)

    def __repr__(self):
        return '<User %r>' % (("%s %s") % (self.given_name, self.family_name))

    def __init__(self, *args, **kwargs):
        # Don't include plain text password in document.
        kwargs.pop('password', None)

        super(User, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Verifies if the given password is the same as the unhashed
        user password.
        
        :param password: Unhashed password
        :type password: string
        :return: True if correct. Otherwise, False.
        :rtype: boolean
        """

        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        """Generates a timed JSON web signature token with a set
        expiration time for authentication.
        
        :param expires_in: Expiration length
        :type expires_in: integer
        :return: Authentication token
        :rtype: string
        """

        serializer = TimedJSONWebSignatureSerializer(
            current_app.config['SECRET_KEY'],
            expires_in=expires_in,
            salt='access'
        )

        return serializer.dumps({
                'id': str(self.id)
            })

    def generate_password_reset_token(self, expires_in):
        """Generates a timed JSON web signature token with a set
        expiration time for resetting a user's password.
        
        :param expires_in: Expiration length
        :type expires_in: integer
        :return: Password reset token
        :rtype: string
        """

        serializer = TimedJSONWebSignatureSerializer(
            current_app.config['SECRET_KEY'],
            expires_in=expires_in,
            salt='password-reset'
        )

        return serializer.dumps({
                'id': str(self.id)
            })

    @staticmethod
    def verify_auth_token(token):
        """Gets the associated User for a given valid authentication
        token.
        
        :param token: Authentication token
        :type token: string
        :return: User associated with the auth token
        :rtype: User model
        """

        serializer = TimedJSONWebSignatureSerializer(
            current_app.config['SECRET_KEY'],
            salt='access'
        )

        try:
            loaded_user = serializer.loads(token.encode('utf-8'))
        except:
            return None

        return User.objects(id=loaded_user['id']).first()

    @staticmethod
    def verify_password_reset_token(token):
        """Gets the associated User for a given valid password reset
        token.
        
        :param token: Password reset token
        :type token: string
        :return: User associated with the password reset token
        :rtype: User model
        """

        serializer = TimedJSONWebSignatureSerializer(
            current_app.config['SECRET_KEY'],
            salt='auth'
        )

        try:
            loaded_user = serializer.loads(token.encode('utf-8'))
        except:
            return None

        return User.objects(id=loaded_user['id']).first()
