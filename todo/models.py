from django.db import models
from django.contrib.auth.models import User




# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.task


# class Registration(models.Model):
#     email = models.TextField(max_length=100)
#     password = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.email



