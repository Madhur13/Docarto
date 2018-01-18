# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20171001_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='big_image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 14, 57, 997516, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 14, 58, 2089, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 14, 58, 1387, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='home_image1',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='home_image2',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='home_image3',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='home_image4',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 12, 14, 58, 2892, tzinfo=utc), null=True, blank=True),
        ),
    ]
