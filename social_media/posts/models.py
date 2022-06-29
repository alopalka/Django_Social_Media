from django.db import models
from django.conf import settings

class Post(models.Model):

    id=models.AutoField(primary_key=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_text=models.TextField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return "{} : {} : {}".format(self.author,self.likes,self.created_at)


class Comment(models.Model):

    id=models.AutoField(primary_key=True)
    post_parent=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_text=models.CharField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField()

    def __str__(self):
        return "{} : {} : {}".format(self.post_parent,self.post_text,self.author)

        

