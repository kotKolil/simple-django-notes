from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Note(models.Model):
    objects = None
    Id = models.IntegerField(unique=True, primary_key=True)
    personal = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    theme = models.TextField()
