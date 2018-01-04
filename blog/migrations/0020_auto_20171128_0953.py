# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_comments_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='commenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('blog_body', models.TextField()),
                ('blog_label', models.CharField(max_length=10)),
                ('blog_about', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存时间')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='comments',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='blog_category',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='commenta',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
        migrations.AddField(
            model_name='commenta',
            name='blog_tags',
            field=models.ManyToManyField(blank=True, to='blog.tags'),
        ),
    ]
