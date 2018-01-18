# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0014_auto_20170813_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='metatags',
            field=models.CharField(default=b'undefined', max_length=1000),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 7, 59, 43, 358602, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 7, 59, 43, 359370, tzinfo=utc), null=True, blank=True),
        ),
    ]
