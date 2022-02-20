from django.shortcuts import render
from .models import Todo
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')


def todo_list(request):
    todos = Todo.objects.all()
    return JsonResponse({'todos': list(todos.values())})
