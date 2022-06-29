from django.contrib import admin
from posts.models import Comment
from posts.models import Post

admin.site.register(Post)
admin.site.register(Comment)