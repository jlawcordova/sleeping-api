# -*- coding: utf-8 -*-
"""
    Todo Resource
    ~~~~~~~~~~~~~

    Contains todos related resources to be accessed from this API.
"""
from http import HTTPStatus
from flask import request
from flask_restful import Resource


class TodosResource(Resource):
    """Serves as a resource for Todo."""

    def get(self):
        """Gets all Todos resource.

        :return: Todo json
        :rtype: werkzeug.Response,
                content-type='application/json', status_code=200
        """
        todos = {
            'todos': [
                {
                    'id': 1,
                    'description': 'Create README file'
                },
                {
                    'id': 2,
                    'description': 'Publish to Github'
                }
            ]
        }
        return todos, HTTPStatus.OK
