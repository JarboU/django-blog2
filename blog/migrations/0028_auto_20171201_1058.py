# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-01 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20171201_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='blog_tags',
            field=models.ManyToManyField(blank=True, to='blog.Tags'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='评论所属文章'),
        ),
    ]
