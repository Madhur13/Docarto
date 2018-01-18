# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20171001_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitedata',
            name='alt_tag1',
            field=models.CharField(default=b'undefined', max_length=50),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='alt_tag2',
            field=models.CharField(default=b'undefined', max_length=50),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='alt_tag3',
            field=models.CharField(default=b'undefined', max_length=50),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='alt_tag4',
            field=models.CharField(default=b'undefined', max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 45, 46, 182440, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 45, 46, 185806, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 45, 46, 185252, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 45, 46, 186440, tzinfo=utc), null=True, blank=True),
        ),
    ]
