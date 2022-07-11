from attr import field
from posts.models import Comment
from posts.models import Post
from django import forms

class CommentForm(forms.ModelForm):

    comment=forms.CharField(max_length=200,widget=forms.Textarea())

    class Meta:
        model=Comment
        fields=["comment"]


class PostForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=["text"]