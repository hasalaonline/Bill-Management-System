# Generated by Django 4.2.2 on 2023-07-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_ceb_amount_nwsdb_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceb',
            name='amount',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='nwsdb',
            name='amount',
            field=models.JSONField(),
        ),
    ]