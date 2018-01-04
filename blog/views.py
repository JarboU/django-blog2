# -*- encoding:utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django import forms, views
from blog import models
import json
import markdown
from blog.models import UpFile, Article, Category
from comments.forms import CommentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index_page(request):
    abcde = models.Article.objects.all().order_by('-create_date')
    return render(request, 'index/index_page.html', context={'abcde': abcde})

def index_category(request, pk=1):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Article.objects.filter(blog_category=cate).order_by('-create_date')
    return render(request, 'index/index_category.html', context={'post_list': post_list})

def index_tags(request):
    return render(request, 'index/index_tags.html')

def archives(request, year, month):
    comments_list = Article.objects.filter(create_date__year=year,
                                            create_date__month=month
                                            ).order_by('-create_date')
    return render(request, 'index/index_list.html', context={'comments_list': comments_list})

def detail(request, pk):
    index_list = models.Article.objects.get(id=pk)
    index_list.blog_body = markdown.markdown(index_list.blog_body,
                                       extension=[
                                           'markdown.extensions.extra',
                                           'markdown.extensions.codehilite',
                                           'markdown.extensions.toc',
                                           'markdown.extensions.fenced_code',
                                           'markdown.extensions.tables'
                                           'markdown.extensions.extensions'
                                       ])
    form = CommentForm()
    comment_list = index_list.comment_set.all()
    context = {'index_list': index_list,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'index/index_list.html', context=context)

class Login(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'error_msg': ''})

    def post(self, request, *args, **kwargs):
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = models.UserInfo.objects.filter(username=user, password=pwd)
        if obj:
            request.session['login'] = True
            request.session['username'] = user
            rep = redirect('/admin/main')
            return rep
        else:
            error_msg = '账号密码错误！'
            return render(request, 'login.html', {'error_msg': error_msg})

def logout(request):
    request.session.clear()
    return redirect('/admin/login')

def admin(request):
    login = request.session.get('login')
    if login:
        current_user = request.session.get('username')
        return render(request, 'admin/main.html', {'username': current_user})
    else:
        return redirect('/admin/login')

def addlist(request):
    if request.method == "GET":
        category = models.Category.objects.all()
        abc = models.Tags.objects.all()
        return render(request, 'admin/add.html', {'category': category, 'abc': abc})
    elif request.method == "POST":
        blog_title = request.POST.get('blog_title', None)
        blog_tags = request.POST.get('blog_tags', None).split(',')
        blog_body = request.POST.get('blog_body', None)
        blog_about = request.POST.get('blog_about', None)
        blog_category = request.POST.get('blog_category')
        #comments_id = models.comments.objects.get(id)
        models.Article.objects.create(blog_title=blog_title, blog_body=blog_body, blog_about=blog_about, blog_category=models.Category.objects.get(id=int(blog_category)), blog_author=models.UserInfo.objects.get(id=1))
        models.Tags.objects.create(name=blog_tags)
        #models.comments.blog_tags.create(tags_id=models.tags.objects.get(id=int(blog_tags)))
        return render(request, 'admin/list.html')

def list(request):
    abcd = models.Category.objects.all()
    abc = models.Tags.objects.all()
    abcde = models.Article.objects.all()
    return render(request, 'admin/list.html', {'abcd': abcd, 'abc': abc, 'abcde': abcde})

def love(request):
    return render(request, 'admin/love.html')

def recycle(request):
    return render(request, 'admin/recycle.html')

def category(request):
    if request.method == "GET":
        category = models.Category.objects.all()
        return render(request, 'admin/category.html', {'category': category})
    elif request.method == "POST":
        name = request.POST.get('name', None)
        models.Category.objects.create(name=name)
        return render(request, 'admin/category.html')

def dela(request):
    if request.method == "Get":
        print('abcd')
    elif request.method == "POST":
        print('abcf')
        dela_a = request.POST['dela_a']
        models.Category.objects.filter(id=dela_a).delete()

class UpFiles(forms.Form):
    upfile = forms.FileField()

def upload(request):
    if request.method == "POST":
        up = UpFiles(request.POST, request.FILES)
        cc = UpFile(up_file=request.FILES['file'])
        cc.save()
        url = 'http://127.0.0.1/' + str(cc.up_file)
        resp = {'success': 1, 'message': "6666", 'url': url}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'success': 0, 'message': "error meth"}
        return HttpResponse(json.dumps(resp), content_type="application/json")