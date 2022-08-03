from django.shortcuts import redirect


def main_view(request):

    if request.user.is_authenticated:
        return redirect('/posts/')
    else:
        return redirect('/auth/login/')
