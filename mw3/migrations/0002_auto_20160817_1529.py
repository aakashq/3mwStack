# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-17 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mw3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuesmodel',
            name='a',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='valuesmodel',
            name='b',
            field=models.FloatField(),
        ),
    ]