from django.shortcuts import render


def main_view(request,template="mainapp/main_page.html"):

    return render(request,template)
