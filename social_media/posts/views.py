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
def react_to_post(request,pk,in_post):
    
    exact_post=Post.objects.get(pk=pk)

    if request.user in exact_post.likes.all():
        exact_post.likes.remove(request.user)
    else:
        exact_post.likes.add(request.user)

    exact_post.save()

    if in_post:
        redirect_to_page=redirect("/posts/details/1")
    else:
        redirect_to_page=redirect("/posts/")

    return redirect_to_page


@login_required
def react_to_comment(request,pk):
    
    exact_comment=Comment.objects.get(pk=pk)

    if request.user in exact_comment.likes.all():
        exact_comment.likes.remove(request.user)
    else:
        exact_comment.likes.add(request.user)

    exact_comment.save()

    return redirect("/posts/details/{}".format(pk))

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

