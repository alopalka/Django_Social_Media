from django.shortcuts import render
from user.models import SocialAccount

def profile_details(request,username,template="user/profile_details.html"):

    user=SocialAccount.objects.get(username=username)

    context={
        'username':username,
    }

    return render(request,template,context)