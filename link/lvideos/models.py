from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=300)
    description = models.CharField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name