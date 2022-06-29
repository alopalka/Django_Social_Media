from django.shortcuts import render
from posts.models import Post
from posts.models import Comment

def main_view(request,template="mainapp/main_page.html"):

    posts=Post.objects.filter()

    context={
        'posts':posts
    }

    return render(request,template,context)
