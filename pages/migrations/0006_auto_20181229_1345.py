# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-29 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20181228_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=b'2018-12-29'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=b'13:45'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='date_added',
            field=models.DateField(default=b'2018-12-29'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(default='', max_length=200, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time_added',
            field=models.TimeField(default=b'13:45'),
        ),
    ]
