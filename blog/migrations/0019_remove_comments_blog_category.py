# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20171127_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='blog_category',
        ),
    ]
