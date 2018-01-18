from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def SignupTask(self, user):
    subject, from_email, to = 'Welcome', 'refernget@gmail.com', user.email
    html_content = render_to_string('base.html')
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject, text_content, from_email,[to])
    msg.attach_alternative(html_content, 'text/html')
