from django.urls import path
from posts import views

app_name="posts"

urlpatterns=[
    path('',views.posts_view,name="posts"),
    path('post/react/<int:pk>/<int:in_post>',views.react_to_post,name="postreact"),
    path('post/details/<int:pk>',views.details_post,name="details"),
    path('post/add',views.create_post,name="postcreate"),
    path('post/delete/<int:pk>',views.delete_post,name="postdelete"),
    path('post/update/<int:pk>',views.update_post,name="postupdate"),
    path('comment/react/<int:pk>',views.react_to_comment,name="commentreact"),
    path('comment/create/<int:pk>',views.create_comment,name="commentcreate"),
]