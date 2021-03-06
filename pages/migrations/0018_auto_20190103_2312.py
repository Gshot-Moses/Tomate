# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-03 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20190103_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField(default=b'2019-01-03')),
                ('time', models.TimeField(default=b'23:12')),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='pages.Adress')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='adress',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(default=b'23:12'),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.TimeField(default=b'23:12'),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=b'23:12'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time_added',
            field=models.TimeField(default=b'23:12'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
