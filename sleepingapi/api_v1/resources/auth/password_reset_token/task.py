# -*- coding: utf-8 -*-
"""
    Password Reset Token Task
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Describe the module in this sentence.

    :copyright: (c) 2018 by Junel Lawrence Cordova.
    :license: MIT, see LICENSE for more details.
"""
from sleepingapi.task import celery


@celery.task()
def send_email(sg_api_client, mail):
    response = sg_api_client.client.mail.send.post(request_body=mail.get())

    return response
