# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-08 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0013_auto_20190408_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='rooms',
        ),
        migrations.AddField(
            model_name='bookings',
            name='rooms',
            field=models.ManyToManyField(blank=True, null=True, to='rooms.Room'),
        ),
    ]
