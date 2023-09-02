# Generated by Django 4.1.4 on 2023-09-02 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_alter_charterflight_message_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ldm',
            name='flight',
        ),
        migrations.AlterField(
            model_name='document',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.charterflight'),
        ),
        migrations.AlterField(
            model_name='file',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.charterflight'),
        ),
        migrations.AlterField(
            model_name='flightproject',
            name='flight',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='flight_project', to='flights.charterflight'),
        ),
        migrations.AlterField(
            model_name='note',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.charterflight'),
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
        migrations.DeleteModel(
            name='LDM',
        ),
    ]