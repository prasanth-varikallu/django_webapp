# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_user_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='text',
            new_name='username',
        ),
    ]