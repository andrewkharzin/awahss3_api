# Generated by Django 4.1.4 on 2023-08-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0013_remove_charterflight_flight_data_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='charterflight',
            name='flight_data_time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]