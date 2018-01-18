from __future__ import absolute_import
from django.core.mail import send_mail, send_mass_mail
from cashback.celery_tasks import app
#from cashback.user_login.models import *
#from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from user_login.models import Customer



@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def SignupTask( email):
    html_content = render_to_string('base.html')
    text_content = strip_tags(html_content)
    send_mail('Welcome', text_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, email], fail_silently=False)

@app.task
def SendOfferEmail(result, cat):
    users = Customer.objects.filter(category__in=[cat]).distinct()
    emails = []
    for user in users:
        emails.append(user.user.email)
    #msg = ('Offers for you', result, settings.EMAIL_HOST_USER, emails)
    send_mail('Offers for U','Hi User !!' , settings.EMAIL_HOST_USER, emails, html_message=result, fail_silently=False)
    return len(emails)
