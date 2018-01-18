# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20170826_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='alt_tag',
            field=models.CharField(default=b'undefined', max_length=50),
        ),
        migrations.AddField(
            model_name='category',
            name='big_image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default=b'Category', max_length=1000),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 10, 41, 829098, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 10, 41, 833042, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 10, 41, 832476, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 10, 41, 833555, tzinfo=utc), null=True, blank=True),
        ),
    ]
