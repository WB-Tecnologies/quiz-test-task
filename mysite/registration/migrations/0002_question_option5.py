# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-16 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option5',
            field=models.CharField(default='', max_length=50),
        ),
    ]
