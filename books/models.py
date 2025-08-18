from django.db import models
from django.db.models import ForeignKey
from django.forms import CharField

class Category(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField
    published_date = models.DateTimeField(null=True,blank=True)
    category = ForeignKey(Category,on_delete=models.CASCADE, related_name="books")
    available_copies = models.PositiveIntegerField(default=1)
    total_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

