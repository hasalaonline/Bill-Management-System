# Generated by Django 4.2.2 on 2023-06-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('ceb', models.CharField(max_length=1000000)),
                ('nwsdb', models.CharField(max_length=1000000)),
            ],
        ),
    ]
