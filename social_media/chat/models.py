from django.db import models
from django.conf import settings

class ChatRoom(models.Model):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user1")
    user2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user2")
    
    
class Message(models.Model):
    
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user")
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True,null=True)
    