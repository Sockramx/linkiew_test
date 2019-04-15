from django.contrib import admin
from .models import Video, Category, SubCategory

class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'description', 'source', 'user', 'category']

    class Meta:
        model = Video

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'subCategory']

    class Meta:
        model = Category

class SubCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    class Meta:
        model = SubCategory


admin.site.register(Video, VideoModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(SubCategory, SubCategoryModelAdmin)