from django import forms
from .models import Tag, Post

class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ('id',)

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('id',)