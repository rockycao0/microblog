# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followed_user',
            field=models.ManyToManyField(default='', related_name='follow', to='account.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='follower_user',
            field=models.ManyToManyField(default='', related_name='follower', to='account.User'),
        ),
    ]