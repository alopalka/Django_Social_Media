from django.urls import path
from posts import views

app_name="posts"

urlpatterns=[
    path('',views.posts_view,name="posts"),
    path('post/react/<int:pk>/<int:in_post>',views.react_to_post,name="reactpost"),
    path('post/details/<int:pk>',views.details_post,name="details"),
    path('comment/react/<int:pk>',views.react_to_comment,name="reactcomment"),
    path('comment/create/<int:pk>',views.create_comment,name="commentcreate"),
]