# Generated by Django 2.1.5 on 2019-02-21 12:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0003_auto_20190217_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('created_time', models.DateTimeField(default=datetime.datetime(2019, 2, 21, 12, 1, 52, 855932, tzinfo=utc))),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bookedusers',
            name='booked_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 12, 1, 52, 853493, tzinfo=utc)),
        ),
    ]
