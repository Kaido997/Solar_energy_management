# Generated by Django 4.0.3 on 2022-03-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solar_energy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('produced', models.IntegerField(null=True)),
                ('consumed', models.IntegerField(null=True)),
            ],
        ),
    ]
