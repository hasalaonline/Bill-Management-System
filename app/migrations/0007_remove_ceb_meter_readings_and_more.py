# Generated by Django 4.2.2 on 2023-07-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_ceb_meter_readings_alter_ceb_units_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ceb',
            name='meter_readings',
        ),
        migrations.RemoveField(
            model_name='nwsdb',
            name='meter_readings',
        ),
        migrations.AddField(
            model_name='ceb',
            name='dues_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ceb',
            name='payments',
            field=models.JSONField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nwsdb',
            name='dues_amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nwsdb',
            name='payments',
            field=models.JSONField(default=0),
            preserve_default=False,
        ),
    ]
