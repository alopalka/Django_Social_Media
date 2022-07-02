from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.models import Comment

@login_required
def posts_view(request,template="posts/posts_page.html"):

    posts=Post.objects.filter()

    context={
        'posts':posts,
    }

    return render(request,template,context)

