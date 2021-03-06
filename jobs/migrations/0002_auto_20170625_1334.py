# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='salary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='client',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.ClientProfile'),
        ),
    ]
