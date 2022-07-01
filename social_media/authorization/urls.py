from django.urls import path
from authorization.views import login_view
from django.contrib.auth import views

app_name="authorization"

urlpatterns=[
    path('login/',login_view,name="login"),
    path('logout/',views.LogoutView.as_view(),name="logout"),
]
