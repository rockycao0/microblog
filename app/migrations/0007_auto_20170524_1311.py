# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-24 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170425_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.CharField(max_length=139),
        ),
    ]