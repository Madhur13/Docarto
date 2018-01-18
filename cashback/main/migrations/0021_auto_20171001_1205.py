# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20170926_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 5, 8, 587246, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 5, 8, 590604, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 5, 8, 590050, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 5, 8, 591254, tzinfo=utc), null=True, blank=True),
        ),
    ]
