from django.urls import path
from posts import views

app_name="posts"

urlpatterns=[
    path('',views.posts_view,name="posts"),
    path('like/<int:pk>',views.like_post,name="like"),
    path('like_comment/<int:pk>',views.like_comment,name="like_comment"),
    path('details/<int:pk>',views.details_post,name="details"),
]