# -*- coding: utf-8 -*-
"""
    SleepingAPI API v1 Blueprint
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The main SleepingAPI blueprint module.
"""
from flask import Blueprint

from .routes import apply_routes

bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')
apply_routes(bp)
