from __future__ import absolute_import
from celery import Celery
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','cashback.settings')
django.setup()
from django.conf import settings

app = Celery('cashback',
             broker='amqp://localhost//',
             include=['cashback.tasks'])


app.config_from_object('django.conf:settings')

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()
