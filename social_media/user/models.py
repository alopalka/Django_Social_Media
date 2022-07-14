from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
        )

        user.username=username
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self,username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )

        user.is_staff = True
        user.admin = True
        user.save()
        return user

# hook in the New Manager to our Model

class SocialAccount(AbstractBaseUser,PermissionsMixin):

    email=models.EmailField(verbose_name="Email address",max_length=255,unique=True)
    username=models.CharField(max_length=255,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    profile_picture=models.ImageField()
    background_picture=models.ImageField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =  ['email']

    objects = UserManager()

