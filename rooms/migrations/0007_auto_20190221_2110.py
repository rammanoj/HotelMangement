# Generated by Django 2.1.5 on 2019-02-21 15:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20190221_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedusers',
            name='booked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 40, 20, 49764, tzinfo=utc)),
        ),
    ]
