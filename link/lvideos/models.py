from django.contrib.auth.models import User
from django.db import models

from categorys.models import Category


class Video(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    link = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=180, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('categorys.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


