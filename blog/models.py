from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    pubished_date = models.DateTimeField(auto_now_add=True)
