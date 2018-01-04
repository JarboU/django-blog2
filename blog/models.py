from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
import django.utils.timezone as timezone

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class UpFile(models.Model):
    up_file = models.FileField(upload_to='upload/')

    def __unicode__(self):
        return self.up_file

class Category(models.Model):
    name = models.CharField(max_length=15)

class Tags(models.Model):
    name = models.CharField(max_length=15)

@python_2_unicode_compatible
class Article(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField()
    blog_about = models.CharField(max_length=50)
    blog_category = models.ForeignKey(Category)
    blog_tags = models.ManyToManyField(Tags, blank=True)
    blog_author = models.ForeignKey(UserInfo)
    create_date = models.DateTimeField(verbose_name="保存时间", default=timezone.now)
    update_date = models.DateTimeField(verbose_name="更新时间", default=timezone.now)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})