from django.conf import settings
from django.db import models


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")
    archived = models.BooleanField(default=False)
    creation_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "{} : {} : {}".format(self.author, self.likes, self.created)


class Comment(models.Model):

    post_parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2048)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="comment_likes", default=False)
    creation_date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "{} : {} : {}".format(self.post_parent, self.comment, self.author)
