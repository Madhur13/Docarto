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
        migrations.AddField(
            model_name='offer',
            name='coupon_code',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 12, 52, 27, 958245, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 12, 52, 27, 961462, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 12, 52, 27, 960876, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 12, 52, 27, 961986, tzinfo=utc), null=True, blank=True),
        ),
    ]
