# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20171001_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandambassador',
            name='fb_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='brandambassador',
            name='profession',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 6, 43, 14, 422985, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 6, 43, 14, 426415, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 6, 43, 14, 425847, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 6, 43, 14, 427048, tzinfo=utc), null=True, blank=True),
        ),
    ]
