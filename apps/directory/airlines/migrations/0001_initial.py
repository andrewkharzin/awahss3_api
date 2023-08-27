# Generated by Django 4.1.4 on 2023-08-25 16:06

import apps.directory.airlines.models.airline
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ageFleet', models.IntegerField(null=True)),
                ('founding', models.IntegerField(null=True)),
                ('sizeAirline', models.IntegerField(null=True)),
                ('statusAirline', models.CharField(blank=True, default='', max_length=155, verbose_name='StatusAirline')),
                ('iataPrefixAccounting', models.IntegerField(null=True)),
                ('callsign', models.CharField(default='', max_length=155, verbose_name='Callsign')),
                ('codeHub', models.CharField(default='', max_length=5, verbose_name='CodeHUB')),
                ('codeIso2Country', models.CharField(blank=True, default='', max_length=4, verbose_name='CodeIso2Country')),
                ('codeIataAirline', models.CharField(default='', max_length=3, verbose_name='Iata')),
                ('codeIcaoAirline', models.CharField(default='', max_length=4, verbose_name='Icao')),
                ('nameAirline', models.CharField(blank=True, default='', max_length=85, verbose_name='Description eng')),
                ('nameCountry', models.CharField(blank=True, default='', max_length=85, null=True, verbose_name='Country')),
                ('type', models.CharField(blank=True, default='', max_length=155, verbose_name='Type')),
                ('arl_logo', models.ImageField(upload_to='airlines/square/')),
                ('cntr_logo', models.ImageField(upload_to='countries/logos/')),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to=apps.directory.airlines.models.airline.airline_banner_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeIataAirline', models.CharField(blank=True, max_length=4, null=True)),
                ('registration_number', models.CharField(max_length=20)),
                ('ac_code', models.CharField(max_length=4)),
                ('model', models.CharField(max_length=100)),
                ('image', models.ImageField(default='airlines/banners/default_ac.jpeg', upload_to=apps.directory.airlines.models.airline.aircraft_image_path)),
                ('airline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='airlines.airline')),
            ],
        ),
    ]
