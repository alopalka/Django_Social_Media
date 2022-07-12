from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from posts.models import Post
from posts.models import Comment
from posts.forms import CommentForm
from posts.forms import PostForm


@login_required
def posts_view(request,template="posts/posts_page.html"):

    posts=Post.objects.filter()
    form=PostForm()

    for post in posts:
        post.amount_of_likes=len(post.likes.all())

    context={
        'form':form,
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
        redirect_to_page=redirect("/posts/post/details/{}".format(pk))
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

    return redirect("/posts/post/details/{}".format(exact_comment.post_parent.pk))


@login_required
def create_comment(request,pk):

    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            raw_form=form.save(commit=False)
            post=Post.objects.get(pk=pk)
            raw_form.post_parent=post
            raw_form.author=request.user
            raw_form.save()
            return redirect("/posts/post/details/{}".format(pk))


@login_required
def create_post(request):

    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            raw_form=form.save(commit=False)
            raw_form.author=request.user
            raw_form.save()

            return redirect("/")


@login_required
def details_post(request,pk,template="posts/posts_details_page.html"):

    post=Post.objects.get(pk=pk)
    post.amount_of_likes=len(post.likes.all())
    comments=Comment.objects.filter(post_parent=post)

    if comments:
        comment_exist=True
    else:
        comment_exist=False

    update_form=PostForm(instance=post)
    form=CommentForm()

    for comment in comments:
        comment.amount_of_likes=len(comment.likes.all())

    context={
        'update_form':update_form,
        'comment_exist':comment_exist,
        'form':form,
        'post':post,
        'comments':comments,
    }

    return render(request,template,context)

@login_required
def delete_post(request,pk):
    post=Post.objects.get(pk=pk)
    if post.author==request.user:
        post.delete()

    return redirect("/")

@login_required
def update_post(request,pk):
    
    found_post=Post.objects.filter(id=pk,author=request.user)

    if request.method=="POST" and found_post:

        form=PostForm(request.POST)
        if form.is_valid():            
            found_post.update(text=form.cleaned_data['text'])
            return redirect("/posts/post/details/{}".format(pk))


    return redirect("/")