from django.contrib import admin
from django.urls import path
from .views import home, todo_list, create_todo, delete, edit

urlpatterns = [
    path('', home, name='home'),
    path('todo_list/', todo_list, name='todo_list'),
    path('create_todo/', create_todo, name='create_todo'),
    path('delete/', delete, name='delete'),
    path('edit/', edit, name='edit'),
]