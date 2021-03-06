# Generated by Django 2.1.5 on 2019-02-16 13:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default=None, max_length=40)),
                ('id_proof', models.FileField(upload_to='uploads/id_proofs/')),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('booked_date', models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 33, 43, 435169, tzinfo=utc))),
                ('status', models.IntegerField(default=1)),
                ('reference', models.CharField(max_length=200)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.BookedUsers')),
            ],
        ),
        migrations.CreateModel(
            name='BookingPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=40)),
                ('status', models.BooleanField(default=False)),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.BookedUsers')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20)),
                ('floor', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=1)),
                ('room_type', models.CharField(choices=[('AC', 'AC Rooms'), ('N-AC', 'Non-AC Rooms')], default='N-AC', max_length=3)),
                ('available', models.BooleanField(default=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Block')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room'),
        ),
    ]
