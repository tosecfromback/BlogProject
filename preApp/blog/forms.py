from django import forms
from .models import Post, Comment, HashTag, Category

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [ 'title', 'content', 'category','writer' ]

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = [ 'content']
        widgets = {
            'content' : forms.Textarea(attrs = {'rows' : '3', 'cols' : '30'})
        }

class HashTagForm(forms.ModelForm):
    
    class Meta:
        model = HashTag
        fields = [ 'name' ]

class Category(forms.ModelForm):

    class Meta:
        model = Category
        fields = [ 'name' ]