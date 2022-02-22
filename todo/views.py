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
        sid = request.POST.get('stuid')
        print("This is a new id" + sid)
        if sid == '':
            todo = Todo.objects.create(task=todo_name)
        else:
            todo = Todo.objects.create(pk=sid, task=todo_name)
        return JsonResponse({'todo_name': todo.task})


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
        selected_id = update_item.id
        print(selected_item)
        print(selected_id)
        return JsonResponse({'selected_item': update_item.task, 'selected_id': selected_id})
