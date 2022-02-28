from django.db import models


# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=100)

    def __str__(self):
        return self.task


class Registration(models.Model):
    email = models.TextField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
