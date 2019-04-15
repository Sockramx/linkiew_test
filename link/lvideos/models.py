from django.db import models

# Create your models here.
class Lvideos(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=300)
    description = models.CharField(max_length=180)

    def __str__(self):
        return self.name