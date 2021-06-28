# Generated by Django 3.2.4 on 2021-06-28 03:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210628_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 28, 3, 1, 12, 985538), max_length=255, verbose_name='Datetime creation'),
        ),
        migrations.AlterField(
            model_name='itap',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 28, 3, 1, 12, 987654)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 28, 3, 1, 12, 985941)),
        ),
    ]
