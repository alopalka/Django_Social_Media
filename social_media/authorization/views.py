from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login


from authorization.forms import RegisterForm

def register_view(request,template="authorization/register_page.html"):

    if request.method == "POST":

        form=RegisterForm(request.POST)

        print(form.errors)

        if form.is_valid():
            form.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
            user=authenticate(username=username,password=password,email=email,request=request)

            return redirect("authorization:login")
    
    else:
        form=RegisterForm()


    context={
        'form':form,
    }

    return render(request,template,context)


def login_view(request, template="authorization/login_page.html"):

    form = AuthenticationForm

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request=request, username=username, password=password)

            login(request, user)
            return redirect("/")

        else:
            return redirect("authorization:login")

    context = {
        'form': form,
    }

    return render(request, template, context)
