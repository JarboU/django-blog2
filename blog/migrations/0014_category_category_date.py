# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20171125_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存时间'),
        ),
    ]
