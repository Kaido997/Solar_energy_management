# Generated by Django 4.0.3 on 2022-04-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0002_alter_solar_energy_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solar_energy',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
