# Generated by Django 2.1.5 on 2019-02-24 06:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20190223_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminlink',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 24, 6, 29, 6, 492879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mobileverification',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 24, 6, 29, 6, 491858, tzinfo=utc)),
        ),
    ]