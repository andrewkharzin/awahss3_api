# Generated by Django 4.1.4 on 2023-09-02 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_remove_ldm_flight_alter_document_flight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightproject',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_project', to='flights.charterflight'),
        ),
    ]