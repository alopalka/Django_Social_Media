from django.shortcuts import render
from user.models import SocialAccount
from posts.models import Post


def profile_details(request, username, template="user/profile_details.html"):

    user = SocialAccount.objects.get(username=username)

    user_posts = Post.objects.filter(author=user)

    for post in user_posts:
        post.amount_of_likes = len(post.likes.all())

    context = {
        'user': user,
        'user_posts': user_posts,
        'username': username,
    }

    return render(request, template, context)
