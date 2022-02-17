from django.contrib import admin
from django.urls import path
from .views import home, todo_list

urlpatterns = [
    path('', home, name='home'),
    path('todo_list/', todo_list, name='todo_list'),
]