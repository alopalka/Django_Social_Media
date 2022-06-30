from django.urls import path
from authorization.views import login_view

app_name="authorization"

urlpatterns=[
    path('login/',login_view,name="login"),
]
