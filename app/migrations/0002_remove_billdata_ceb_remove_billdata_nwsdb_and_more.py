# Generated by Django 4.2.2 on 2023-06-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billdata',
            name='ceb',
        ),
        migrations.RemoveField(
            model_name='billdata',
            name='nwsdb',
        ),
        migrations.AddField(
            model_name='billdata',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='billdata',
            name='meter_reading',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billdata',
            name='month',
            field=models.CharField(default='June', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='billdata',
            name='platform',
            field=models.CharField(default='Unknown', max_length=10),
            preserve_default=False,
        ),
    ]