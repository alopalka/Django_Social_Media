from django.urls import path
from posts import views

app_name="posts"

urlpatterns=[
    path('',views.posts_view,name="posts"),
    path('react_to_post/<int:pk>/<int:in_post>',views.react_to_post,name="reactpost"),
    path('react_to_comment/<int:pk>',views.react_to_comment,name="reactcomment"),
    path('details/<int:pk>',views.details_post,name="details"),
]