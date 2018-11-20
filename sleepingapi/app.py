# -*- coding: utf-8 -*-
"""
    SleepingAPI App
    ~~~~~~~~~~~~~~~

    The main SleepingAPI app module.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from flask import Flask, g
from werkzeug.utils import find_modules, import_string

from .api_v1 import bp
from .config import CONFIG
from .database import db
from .schema import ma

APP_ENVVAR_SETTINGS = 'SLEEPING_API_SETTINGS'
APP_PYFILE_SETTINGS = 'application.cfg'

def create_app(config_name):
    """Creates the application instance."""
    app = Flask(__name__, instance_relative_config=True)

    # Set up configuration.
    app.config.from_object(CONFIG[config_name])
    app.config.from_pyfile(APP_PYFILE_SETTINGS)
    app.config.from_envvar(APP_ENVVAR_SETTINGS, silent=True)

    # Apply the database extension.
    db.init_app(app)

    # Apply the schema extension.
    ma.init_app(app)

    # Register the blueprints.
    app.register_blueprint(bp)

    return app