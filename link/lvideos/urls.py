from django.urls import path
from .views import home, list, create, edit, delete 

app_name = 'videos'
urlpatterns = [
    path('home/', home, name='home'),
    path('list/', list, name='list'),
    path('create/', create, name='create'),
    path('edit/<int:video_id>', edit, name='edit'),
    path('delete/<int:video_id>', delete, name='delete'),
]
