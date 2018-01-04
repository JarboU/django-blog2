# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20171125_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='blog_date',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
        migrations.AddField(
            model_name='comments',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间'),
        ),
    ]