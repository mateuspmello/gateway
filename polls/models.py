from django.db import models
from django.core import serializers
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField("date published", null=True)
    content = models.CharField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='post_author')