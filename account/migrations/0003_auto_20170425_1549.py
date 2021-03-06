# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20170423_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followed_user',
        ),
        migrations.AddField(
            model_name='user',
            name='followed_user',
            field=models.ManyToManyField(to='account.User'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='follower_user',
        ),
        migrations.AddField(
            model_name='user',
            name='follower_user',
            field=models.ManyToManyField(related_name='follower', to='account.User'),
        ),
    ]
