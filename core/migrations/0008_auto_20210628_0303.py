# Generated by Django 3.2.4 on 2021-06-28 03:03

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210628_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverification',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime.now, max_length=255, verbose_name='Datetime creation'),
        ),
        migrations.AlterField(
            model_name='itap',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
