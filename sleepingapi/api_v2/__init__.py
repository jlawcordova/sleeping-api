# -*- coding: utf-8 -*-
"""
    SleepingAPI API v2 Blueprint
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The main SleepingAPI blueprint module.
"""
from flask import Blueprint

from .routes import apply_routes

bp = Blueprint('api_v2', __name__, url_prefix='/api/v2')
apply_routes(bp)
