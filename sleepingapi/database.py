# -*- coding: utf-8 -*-
"""
    SleepingAPI Database
    ~~~~~~~~~~~~~~~~~~~~

    The main SleepingAPI database module.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from werkzeug.exceptions import BadRequest, Conflict, UnprocessableEntity, \
    ServiceUnavailable

from flask_mongoengine import MongoEngine as MongoEngineBase
from mongoengine.errors import ValidationError, FieldDoesNotExist, \
    OperationError, NotUniqueError
from pymongo.errors import ServerSelectionTimeoutError, AutoReconnect


class MongoEngine(MongoEngineBase):
    """Extends the MongoEngine extension with custom context managers."""

    class QueryContext(object):
        """Handles queries performed to the database. Raises proper Werkzeug
        exceptions when errors occur.

        Example::

            with db.QueryContext():
                Foo(**foo).save()
        """

        def __enter__(self):
            pass

        def __exit__(self, type, value, traceback):
            """Raises the proper exceptions when exiting the context manager
            with errors.

            :raises Conflict: occurs when a duplicate data is being inserted in
                              a unique field.
            :raises UnprocessableEntity: occurs when query data is invalid.
            :raises ServiceUnavailable: occurs when the database service
                                        becomes inaccessible.
            """

            # Validation errors.
            if isinstance(value, ValidationError):
                errors = {}
                if value.errors is not None:
                    errors = {
                        key: [value.errors[key].message]
                        for key in value.errors.keys()
                    }
                else:
                    errors = {
                        value.field_name: [value.message]
                    }
                validation_errors = {
                    'errors': errors
                }
                raise UnprocessableEntity(validation_errors)
            if isinstance(value, FieldDoesNotExist):
                errors = {
                    'errors': {
                        'name': 'non_existent_field',
                        'description': value.args[0]
                    }
                }
                raise UnprocessableEntity(errors)

            # Conflict errors.
            if isinstance(value, NotUniqueError):
                errors = {
                    'errors': {
                        'name': 'not_unique',
                        'description': value.args[0]
                    }
                }
                raise Conflict(errors)
            if isinstance(value, OperationError):
                errors = {
                    'errors': {
                        'name': 'failed_operation',
                        'description': value.args[0]
                    }
                }
                raise Conflict(errors)

            # Unavailable service errors.
            if isinstance(value, ServerSelectionTimeoutError):
                errors = {
                    'errors': {
                        'name': 'server_selection_timeout_error',
                        'description': value.args[0]
                    }
                }
                raise ServiceUnavailable(errors)
            if isinstance(value, AutoReconnect):
                errors = {
                    'errors': {
                        'name': 'auto_reconnect',
                        'description': value.args[0]
                    }
                }
                raise ServiceUnavailable(errors)


db = MongoEngine()  # pylint: disable=C0103
