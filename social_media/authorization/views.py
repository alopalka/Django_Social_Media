from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login


def login_view(request,template="auth/login_page.html"):

    form=AuthenticationForm

    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request=request,username=username,password=password)

            login(request,user)
            return redirect("/")

        else:
            return redirect("authorization:login")
    
    context={
        'form':form,
    }

    return render(request,template,context)