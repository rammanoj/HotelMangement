# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-18 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0017_auto_20190415_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_no',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
