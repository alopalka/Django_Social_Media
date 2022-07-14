from django.shortcuts import render

def profile_details(request,username,template="user/profile_details.html"):

    context={
        'username':username,
    }

    return render(request,template,context)