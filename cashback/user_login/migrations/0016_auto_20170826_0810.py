# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0015_auto_20170826_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='alt_tag',
            field=models.CharField(default=b'undefined', max_length=50),
        ),
        migrations.AddField(
            model_name='company',
            name='big_image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(default=b'Company', max_length=1000),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 10, 41, 830278, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 10, 41, 831249, tzinfo=utc), null=True, blank=True),
        ),
    ]
