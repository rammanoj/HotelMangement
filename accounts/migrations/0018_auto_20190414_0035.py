# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-14 00:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20190414_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlink',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 0, 35, 35, 848357)),
        ),
        migrations.AlterField(
            model_name='mobileverification',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 0, 35, 35, 847773)),
        ),
    ]
