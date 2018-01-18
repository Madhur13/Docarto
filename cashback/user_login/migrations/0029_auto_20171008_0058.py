# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0028_auto_20171007_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='page_description',
            field=models.CharField(default=b'undefined', max_length=1000),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 7, 19, 28, 51, 904006, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 7, 19, 28, 51, 904745, tzinfo=utc), null=True, blank=True),
        ),
    ]
