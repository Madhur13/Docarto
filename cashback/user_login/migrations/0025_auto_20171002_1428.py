# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0024_auto_20171002_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 14, 28, 42, 292096, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 14, 28, 42, 292822, tzinfo=utc), null=True, blank=True),
        ),
    ]
