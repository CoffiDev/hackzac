# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20170625_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='interest_area',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='level',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
