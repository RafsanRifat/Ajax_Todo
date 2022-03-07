from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from django.db.models.manager import EmptyManager
from .models import Profile



class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

    class AnonymousUser:
        is_staff = True
        is_active = True
        is_superuser = True
        _groups = EmptyManager(Group)
        _user_permissions = EmptyManager(Permission)





# class UserCreationForm(UserCreationForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#         help_texts = {
#             'username': None,
#             'email': None,
#             'password1': None,
#             'password2': None,
#         }
#
#     class AnonymousUser:
#         is_staff = True
#         is_active = True
#         is_superuser = True
#         _groups = EmptyManager(Group)
#         _user_permissions = EmptyManager(Permission)
