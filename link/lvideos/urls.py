from django.urls import path
from .views import home, list, create, edit, delete 

app_name = 'videos'
urlpatterns = [
    path('home/', home, name='home'),
    path('list/', list, name='list'),
    path('create/', create, name='create'),
    path('edit/', edit, name='edit'),
    path('delete/', delete, name='delete'),
]
