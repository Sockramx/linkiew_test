from django.contrib import admin
from .models import Video

class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'description', 'source', 'user', 'category']

    class Meta:
        model = Video



admin.site.register(Video, VideoModelAdmin)
