from django.conf.urls import url
from . import views
from django.conf.urls.static import static
import os
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.index_category, name='category'),
    url(r'^uploadfile$', views.upload, name='upload'),
    url(r'^admin/list$', views.list),
    url(r'^logout/', views.logout),
]

media_root = os.path.join(settings.BASE_DIR, 'upload')
urlpatterns += static('/upload/', document_root=media_root)
