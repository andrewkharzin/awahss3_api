# Generated by Django 4.1.4 on 2023-08-26 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='date',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='time',
        ),
        migrations.AddField(
            model_name='flight',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]