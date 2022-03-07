from django.contrib import admin
from django.urls import path
from .views import home, todo_list, create_todo, delete, edit, registration_home, todo_login, todo_logout, verification

urlpatterns = [
    path('', home, name='home'),
    path('todo_list/', todo_list, name='todo_list'),
    path('create_todo/', create_todo, name='create_todo'),
    path('delete/', delete, name='delete'),
    path('todos/<int:pk>/', edit, name='edit'),
    path('registration_home/', registration_home, name='registration_home'),
    path('login/', todo_login, name='login'),
    path('logout/', todo_logout, name='logout'),
    path('verify/', verification, name='verify'),
]
