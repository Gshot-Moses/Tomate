# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-29 13:14
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20181229_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=b'14:14'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(default='None', max_length=200, storage=django.core.files.storage.FileSystemStorage(location='/images/profile'), upload_to=b''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time_added',
            field=models.TimeField(default=b'14:14'),
        ),
    ]
