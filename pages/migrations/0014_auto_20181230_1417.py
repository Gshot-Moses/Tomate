# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-30 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20181230_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='pages.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(default=b'14:17'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='pages.UserInfo'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='pages.Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.TimeField(default=b'14:17'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='pages.UserInfo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=b'14:17'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time_added',
            field=models.TimeField(default=b'14:17'),
        ),
    ]
