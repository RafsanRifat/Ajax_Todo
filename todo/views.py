from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.crypto import get_random_string

from .models import Todo, Profile
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationForm
from django.core.serializers import serialize
from django.core.mail import send_mail
from django.conf import settings


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


def generateOTP():
    short_code = get_random_string(length=6, allowed_chars='A@$0BF5RH8LUTafbwty79%&')
    print(short_code)
    return short_code


def registration_home(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = request.POST.get('email')
        otpCode = generateOTP()
        print(email)
        send_mail(
            # subject :
            'OTP',

            # Message :
            'This is your OTP code. Please Use this OTP code To confirm your account : ' + otpCode,

            # from_email:
            settings.EMAIL_HOST_USER,

            # recipient_list:
            [email],
        )

        if form.is_valid():
            username = request.POST.get('username')
            print(username)
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=True,
                is_superuser=True,
                is_active=False,
            )
            Profile.objects.create(user=user, otp=otpCode)
            user.save()

        else:
            return JsonResponse({
                'errors': form.errors
            })

        return JsonResponse({'Message': 'User created successfully'})


    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def verification(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        otp = request.POST.get('otp')
        user = User.objects.filter(username=username).first()
        # print(otp)
        print(user.username)

        otp = user.profile.otp
        print(otp)

        if user.username == username and user.profile.otp == otp:

            if user.is_active == False:
                user.is_active = True
                user.save()
        else:
            return JsonResponse({'error_verification': 'username or OTP is not matching'})

    return render(request, 'verify.html')


def todo_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return JsonResponse({'error_message': 'Invalid email or password'})
    return render(request, 'login.html')


def todo_logout(request):
    logout(request)
    return render(request, 'login.html')

# def registration(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         new_user = Registration.objects.create(email=email, password=password)
#         new_user.save()
#         return JsonResponse({'message': 'Congratulation ! you have successfully created your account'})
