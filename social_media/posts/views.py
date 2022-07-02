from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from posts.models import Post
from posts.models import Comment

@login_required
def posts_view(request,template="posts/posts_page.html"):

    posts=Post.objects.filter()

    for post in posts:
        post.amount_of_likes=len(post.likes.all())

    context={
        'posts':posts,
    }

    return render(request,template,context)


@login_required
def like_post(request,pk):
    
    exact_post=Post.objects.get(pk=pk)
    exact_post.likes.add(request.user)
    exact_post.save()


    return redirect("/")


@login_required
def like_comment(request,pk):
    
    exact_comment=Comment.objects.get(pk=pk)
    exact_comment.likes.add(request.user)
    exact_comment.save()


    return redirect("/")

@login_required
def details_post(request,pk,template="posts/posts_details_page.html"):

    post=Post.objects.get(pk=pk)

    post.amount_of_likes=len(post.likes.all())

    comments=Comment.objects.filter(post_parent=post)

    for comment in comments:
        comment.amount_of_likes=len(post.likes.all())

    context={
        'post':post,
        'comments':comments,
    }

    return render(request,template,context)

