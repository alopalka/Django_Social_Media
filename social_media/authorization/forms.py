from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import SocialAccount

class RegisterForm(UserCreationForm):

    class Meta:
        model=SocialAccount
        fields=['email','username','password1','password2']
