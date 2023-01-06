from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    author=models.CharField(max_length=100)
    title=models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    content=models.ForeignKey(User, on_delete=models.CASCADE)
    