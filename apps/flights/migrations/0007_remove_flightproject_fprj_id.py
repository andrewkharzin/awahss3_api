# Generated by Django 4.1.4 on 2023-09-02 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_alter_flightproject_flight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightproject',
            name='fprj_id',
        ),
    ]
