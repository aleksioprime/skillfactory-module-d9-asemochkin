from django.db import models  
from django.utils import timezone 
from django.contrib.auth.models import User 

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'

class Post(models.Model):  
    title = models.CharField(max_length=255)  
    slug = models.SlugField 
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])  
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)  
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True, related_name='posts')
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}'