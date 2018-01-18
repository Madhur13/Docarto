# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 18:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170703_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 4, 18, 18, 59, 125199, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 4, 18, 18, 59, 125199, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 4, 18, 18, 59, 125199, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 4, 18, 18, 59, 125199, tzinfo=utc), null=True),
        ),
    ]
