# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20170719_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 21, 6, 33, 929586, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 21, 6, 34, 108876, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 21, 6, 34, 107494, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 21, 6, 34, 110350, tzinfo=utc), null=True, blank=True),
        ),
    ]
