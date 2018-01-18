# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20171004_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='expired',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 7, 13, 45, 17, 49651, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 7, 13, 45, 17, 81573, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 7, 13, 45, 17, 78527, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 7, 13, 45, 17, 85077, tzinfo=utc), null=True, blank=True),
        ),
    ]
