# Generated by Django 4.1.4 on 2023-09-14 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shc',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
