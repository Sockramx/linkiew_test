from django.urls import path
from .views import home, list, create, edit, delete 

app_name = 'categorys'
urlpatterns = [
    path('home/', home, name='home'),
    path('list/', list, name='list'),
    path('create/', create, name='create'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
]
