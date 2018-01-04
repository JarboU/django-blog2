from ..models import Tags, Category, Article
from django import template

register = template.Library()

@register.simple_tag
def get_tags():
    return Tags.objects.all()

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_date():
    return Article.objects.dates('create_date', 'month', order='DESC')

