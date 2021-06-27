# Generated by Django 3.2.4 on 2021-06-25 02:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210625_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='emailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=32, unique=True)),
                ('token', models.CharField(default='null', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='itap',
            name='activation_date',
            field=models.DateField(verbose_name=datetime.datetime(2021, 6, 25, 2, 18, 27, 366842, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]