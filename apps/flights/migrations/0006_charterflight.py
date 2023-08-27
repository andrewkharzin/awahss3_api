# Generated by Django 4.1.4 on 2023-08-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_alter_flight_flight_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharterFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(blank=True, max_length=20, null=True)),
                ('aircraft_type', models.CharField(blank=True, max_length=50, null=True)),
                ('registration_number', models.CharField(blank=True, max_length=20, null=True)),
                ('flight_route', models.CharField(blank=True, max_length=100, null=True)),
                ('departure_iata', models.CharField(blank=True, max_length=3)),
                ('arrival_iata', models.CharField(blank=True, max_length=4)),
                ('segment_route', models.CharField(blank=True, max_length=100)),
                ('segment_date_time', models.DateTimeField(blank=True, null=True)),
                ('segment_description', models.TextField(blank=True)),
            ],
        ),
    ]