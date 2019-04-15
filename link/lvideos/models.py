from django.contrib.auth.models import User
from django.db import models



class SubCategory(models.Model):
    name = models.CharField(max_length=50, blank=True , null=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    link = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=180, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


