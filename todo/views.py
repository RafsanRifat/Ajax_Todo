from django.shortcuts import render
from .models import Todo
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'index.html')


def todo_list(request):
    todos = Todo.objects.all()
    return JsonResponse({'todos': list(todos.values())})

def create_todo(request):
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo = Todo.objects.create(task=todo_name)
        print(todo_name)
        return JsonResponse({'todo_name': todo_name})
