# Generated by Django 2.1.5 on 2019-02-16 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 43, 17, 765702, tzinfo=utc)),
        ),
    ]
