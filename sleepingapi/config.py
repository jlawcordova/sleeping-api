# -*- coding: utf-8 -*-
"""
    Configuration
    ~~~~~~~~~~~~~

    The configuration module for Sleeping API.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
# pylint: disable=r0903


class Config(object):
    """The base configuration class."""
    DEBUG = False

    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'

    ACCESS_TOKEN_DURATION = 3600
    PASSWORD_RESET_TOKEN_DURATION = 3600


class DevelopmentConfig(Config):
    """The development configuration class."""
    DEBUG = True


class StagingConfig(Config):
    """The staging configuration class."""
    pass


class ProductionConfig(Config):
    """The production configuration class."""
    pass


CONFIG = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}
