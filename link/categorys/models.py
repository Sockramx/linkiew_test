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