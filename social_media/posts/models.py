from django.db import models
from django.conf import settings

class Post(models.models):

    id=models.AutoField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_text=models.CharField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField()

    def __str__(self):
        return "{} : {} : {}".format(self.user,self.likes,self.created_at)
        

