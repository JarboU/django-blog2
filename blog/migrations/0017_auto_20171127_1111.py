# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20171125_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('blog_body', models.TextField()),
                ('blog_label', models.CharField(max_length=10)),
                ('blog_category', models.CharField(max_length=15)),
                ('blog_about', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存时间')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
            ],
        ),
        migrations.DeleteModel(
            name='comments',
        ),
    ]
