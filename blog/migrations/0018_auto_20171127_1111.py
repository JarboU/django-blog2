# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20171127_1111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comment',
            new_name='comments',
        ),
    ]
