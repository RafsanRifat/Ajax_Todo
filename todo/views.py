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
        todo_id = todo.id
        print(todo_id)
        return JsonResponse({'todo_name': todo.task, 'todo_id': todo_id})


def delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        item = Todo.objects.get(pk=id)
        item.delete()
        return JsonResponse({'status': 1})


def edit(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        update_item = Todo.objects.get(pk=id)
        selected_item = update_item.task
        print(selected_item)
        return JsonResponse({'selected_item': update_item.task})
