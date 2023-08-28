# Generated by Django 4.1.4 on 2023-08-28 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0012_rename_departure_iata_charterflight_iata_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charterflight',
            name='flight_data_time',
        ),
        migrations.AddField(
            model_name='charterflight',
            name='flight_data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='charterflight',
            name='flight_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]