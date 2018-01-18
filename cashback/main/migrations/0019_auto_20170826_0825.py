# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20170826_0810'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('home_image1', models.ImageField(null=True, upload_to=b'')),
                ('home_image2', models.ImageField(null=True, upload_to=b'')),
                ('home_image3', models.ImageField(null=True, upload_to=b'')),
                ('home_image4', models.ImageField(null=True, upload_to=b'')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 25, 58, 940520, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 25, 58, 943886, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 25, 58, 943319, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 26, 8, 25, 58, 944399, tzinfo=utc), null=True, blank=True),
        ),
    ]
