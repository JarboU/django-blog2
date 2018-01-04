# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171124_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='blog_category',
        ),
    ]