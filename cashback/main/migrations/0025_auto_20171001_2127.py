# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0023_auto_20171001_2127'),
        ('main', '0024_auto_20171001_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandAmbassador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('fb_url', models.URLField()),
                ('profession', models.IntegerField()),
                ('why', models.CharField(max_length=1000, null=True, blank=True)),
                ('how', models.CharField(max_length=1000, null=True, blank=True)),
                ('interests', models.CharField(max_length=1000, null=True, blank=True)),
                ('customer', models.ForeignKey(to='user_login.Customer')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 21, 27, 35, 490901, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 21, 27, 35, 494302, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 21, 27, 35, 493739, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 21, 27, 35, 494929, tzinfo=utc), null=True, blank=True),
        ),
    ]
