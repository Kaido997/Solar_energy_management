# Generated by Django 4.0.3 on 2022-04-04 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0004_alter_solar_energy_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solar_energy',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 4, 15, 13, 58, 769806, tzinfo=utc)),
        ),
    ]
