from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article
from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request, post_pk):
    post = get_object_or_404(Article, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            dd = form.cleaned_data
            comment = form.save(False)
            comment.name = dd['name']
            comment.email = dd['email']
            comment.article = Article.objects.get(id=post_pk)
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'index/index_list.html', context=context)
    return redirect(post)