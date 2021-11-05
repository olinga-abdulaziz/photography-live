from django import forms
from django.forms import fields, widgets
from .models import Post,Category

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title","author","category","title_tag","body")


        widgets={
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "author": forms.Select(attrs={'class':'form-control'}),
            "category": forms.Select(attrs={'class':'form-control'}),
            "title_tag": forms.TextInput(attrs={'class':'form-control'}),
            "body": forms.Textarea(attrs={'class':'form-control'}),
        }