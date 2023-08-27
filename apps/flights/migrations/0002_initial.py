# Generated by Django 4.1.4 on 2023-08-25 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flights', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('airlines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightproject',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flightproject',
            name='documents',
            field=models.ManyToManyField(blank=True, to='flights.document'),
        ),
        migrations.AddField(
            model_name='flightproject',
            name='files',
            field=models.ManyToManyField(blank=True, to='flights.file'),
        ),
        migrations.AddField(
            model_name='flightproject',
            name='flight',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='flight_project', to='flights.flight'),
        ),
        migrations.AddField(
            model_name='flightproject',
            name='notes',
            field=models.ManyToManyField(blank=True, to='flights.note'),
        ),
        migrations.AddField(
            model_name='flight',
            name='aircraft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='airlines.aircraft'),
        ),
        migrations.AddField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='airlines.airline'),
        ),
        migrations.AddField(
            model_name='flight',
            name='ldm_telex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flighs', to='flights.ldm'),
        ),
        migrations.AddField(
            model_name='file',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight'),
        ),
        migrations.AddField(
            model_name='file',
            name='flight_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flightproject'),
        ),
        migrations.AddField(
            model_name='document',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight'),
        ),
        migrations.AddField(
            model_name='document',
            name='flight_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flightproject'),
        ),
    ]
