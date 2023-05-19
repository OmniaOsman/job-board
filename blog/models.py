from django.db import models 
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.shortcuts import reverse
from autoslug import AutoSlugField


# Create your models here.
class Post(models.Model):
    title        = models.CharField(max_length=150)
    body         = models.TextField()
    author       = models.ForeignKey(User, on_delete=models.CASCADE)
    tags         = TaggableManager()
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug         = AutoSlugField(populate_from='title', unique=True)
    category     = models.ForeignKey('Category', 
                                     related_name='post_category', 
                                     on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
              

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug  = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

