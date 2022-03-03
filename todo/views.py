from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
from django.core.serializers import serialize


# Create your views here.
def home(request):
    return render(request, 'index.html')


def todo_list(request):
    # todos = Todo.objects.all()
    todos = Todo.objects.filter(user=request.user).all()
    return JsonResponse({'todos': list(todos.values())})
    # return JsonResponse({'user': list(user)})


def create_todo(request):
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        sid = request.POST.get('stuid')
        print("This is a new id" + sid)
        todo = Todo.objects.create(task=todo_name, user=request.user)
        todo_name = todo.task
        return JsonResponse({'todo_name': todo.task, 'sid': sid})


def delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        item = Todo.objects.get(pk=id)
        item.delete()
        return JsonResponse({'status': 1})


def edit(request, pk):
    item = get_object_or_404(Todo, pk=pk)

    if request.method == 'POST':
        item.task = request.POST.get('title')
        item.save()

    return JsonResponse({
        'task': item.task,
        'update_id': item.id
    })


def registration_home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            print(username)
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')

            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
        else:
            return JsonResponse({
                'errors': form.errors
            })

        return JsonResponse({'Message': 'User created successfully'})


    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

# def registration(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         new_user = Registration.objects.create(email=email, password=password)
#         new_user.save()
#         return JsonResponse({'message': 'Congratulation ! you have successfully created your account'})
