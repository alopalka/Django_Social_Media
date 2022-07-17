from django.db import models
from django.conf import settings

class Room(models.Model):
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
    
class Message(models.Model):
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True,null=True)
    