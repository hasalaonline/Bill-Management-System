# Generated by Django 4.2.2 on 2023-06-30 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_ceb_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceb',
            name='meter_readings',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='ceb',
            name='units',
            field=models.JSONField(default=dict),
        ),
    ]