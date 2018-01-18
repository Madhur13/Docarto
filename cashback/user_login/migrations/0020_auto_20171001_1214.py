# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0019_auto_20171001_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='big_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 14, 57, 998984, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 14, 57, 999853, tzinfo=utc), null=True, blank=True),
        ),
    ]
