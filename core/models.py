from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        
        return reverse('home', kwargs={'pk': self.pk})

class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title_tag=models.CharField(max_length=255)
    body=RichTextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.pk})


