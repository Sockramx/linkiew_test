from django.urls import path
from .views import videos, home

app_name = 'videos'
urlpatterns = [
    path('home/', home, name='home'),
    path('list/', videos, name='list'),
]
