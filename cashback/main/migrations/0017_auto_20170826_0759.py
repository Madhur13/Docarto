# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='metatags',
            field=models.CharField(default=b'undefined', max_length=1000),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 7, 59, 43, 357988, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 7, 59, 43, 361162, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 7, 59, 43, 360594, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 7, 59, 43, 361677, tzinfo=utc), null=True, blank=True),
        ),
    ]
