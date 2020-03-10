# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-30 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20181230_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(default=b'14:14'),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.TimeField(default=b'14:14'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=b'14:14'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='pages.UserInfo'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time_added',
            field=models.TimeField(default=b'14:14'),
        ),
    ]
