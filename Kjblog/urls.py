"""Kjblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from blog import views
import os
from django.conf import settings

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^index', views.index),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    #url(r'^admin/login/', views.login),
    #等于下面
    url(r'^admin/login/', views.Login.as_view()),
    url(r'^admin/main/$', views.admin),
    #url(r'^templates/admin/add$', views.add),
    url(r'^admin/love$', views.love),
    url(r'^admin/recycle$', views.recycle),
    #url(r'^templates/admin/', include('blog.urls')),
    url(r'^admin/add$', views.addlist),
    url(r'^admin/category$', views.category),
    url(r'^dela$', views.dela),
    url(r'^index/index_page', views.index_page),
    #url(r'^admin/', include('blog.urls')),
    url(r'^category', views.index_category),
    url(r'^tags', views.index_tags),
]