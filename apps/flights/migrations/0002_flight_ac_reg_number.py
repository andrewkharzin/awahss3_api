# Generated by Django 4.1.4 on 2023-08-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='ac_reg_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]
