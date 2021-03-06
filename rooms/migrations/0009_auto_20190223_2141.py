# Generated by Django 2.1.5 on 2019-02-23 16:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20190222_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedusers',
            name='booked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 23, 16, 11, 49, 820655, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('AC', 'AC Rooms'), ('N-AC', 'Non-AC Rooms')], default='N-AC', max_length=5),
        ),
    ]
