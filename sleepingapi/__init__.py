# -*- coding: utf-8 -*-
"""
    SleepingAPI Init
    ~~~~~~~~~~~~~~~~

    Places the application instance at the top level of the module.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
import os

from celery import Celery

from .config import Config
from .app import create_app
from .task import celery

APP_CONFIG = 'SLEEPING_API_CONFIG'

app = create_app(os.getenv(APP_CONFIG) or 'default')  # pylint: disable=C0103
