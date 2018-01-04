from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.

# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField('评论者名字', max_length=100)
    email = models.EmailField('评论者邮箱', max_length=255)
    url = models.URLField('评论者链接', blank=True)
    text = models.TextField('评论内容')
    create_date = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('blog.Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]