# -*- coding: utf-8 -*-
"""
    Sleeping API Setup
    ~~~~~~~~~~~~~~~~~~

    Sets up the Sleeping API application as a package.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup, find_packages


setup(
    name='SleepingAPI',
    version='1.0.0',
    description='Sleeping API is a base project for creating RESTful API '
    'applications with Flask.',
    long_description='Sleeping API is a base project for creating RESTful '
    'API with Flask.',
    url='sleepingapi.com',
    author='Junel Lawrence Cordova',
    author_email='jlaw.cordova@gmail.com',
    license='MIT',
    platforms='any',
    packages=[
        'sleepingapi'
    ],
    include_package_data=True,
    install_requires=[
        'flask>=0.12.3',
        'Flask-RESTful==0.3.6',
        'Flask-Marshmallow==0.8.0',
        'Flask-Mongoengine==0.9.5',
        'Marshmallow-Mongoengine==0.9.1',
        'Flask-HTTPAuth==3.2.3',
        'celery==4.1.0'
    ]
)
