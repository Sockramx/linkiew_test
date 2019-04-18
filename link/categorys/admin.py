from django.contrib import admin
from .models import Category, SubCategory



class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'subCategory']

    class Meta:
        model = Category

class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    class Meta:
        model = SubCategory


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(SubCategory, SubCategoryModelAdmin)