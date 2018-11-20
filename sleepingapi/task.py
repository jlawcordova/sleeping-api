# -*- coding: utf-8 -*-
"""
    SleepingAPI Task
    ~~~~~~~~~~~~~~~~

    The main SleepingAPI task queueing module.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from .config import Config
from celery import Celery

celery = Celery(__name__, backend=Config.CELERY_RESULT_BACKEND,
                broker=Config.CELERY_BROKER_URL)
