# Generated by Django 4.1.4 on 2023-08-27 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0011_charterflight_flight_data_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charterflight',
            old_name='departure_iata',
            new_name='iata',
        ),
        migrations.RenameField(
            model_name='charterflight',
            old_name='arrival_iata',
            new_name='icao',
        ),
    ]
