# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-03 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20190103_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.TimeField(default=b'23:16'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(default=b'23:16'),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.TimeField(default=b'23:16'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=b'23:16'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time_added',
            field=models.TimeField(default=b'23:16'),
        ),
    ]
