from django.urls import path
from posts import views

app_name="posts"

urlpatterns=[
    path('',views.posts_view,name="posts"),
    path('like/<int:pk>',views.like_post,name="like"),
    path('details/<int:pk>',views.details_post,name="details")
]