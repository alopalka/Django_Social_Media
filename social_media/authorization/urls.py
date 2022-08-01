from django.urls import path
from authorization import views
from django.contrib.auth import views as auth_views

app_name="authorization"

urlpatterns=[
    path('login/',views.login_view,name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('register/',views.register_view,name="register"),
]
