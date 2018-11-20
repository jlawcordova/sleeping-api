# -*- coding: utf-8 -*-
"""
    Email 
    ~~~~~

    Contains emailing utilities using SendGrid as an email delivery
    service and Celery for email sending task queueing.
"""
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Email as SendGridEmail, Mail


class SendGridMailFactory(object):

    def create_mail(self, from_email, to_email, subject, content):
        from_email = SendGridEmail("support@sleepingapi.com")
        to_email = SendGridEmail("jlaw.cordova@gmail.com")
        subject = "Sending with SendGrid is Fun"
        content = Content(
            "text/plain", "and easy to do anywhere, even with Python")
        mail = Mail(from_email, subject, to_email, content)

        return mail
