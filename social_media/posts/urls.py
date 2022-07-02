from django.urls import path
from posts import views

app_name="posts"

urlpatterns=[
    path('',views.posts_view,name="posts")
]