from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Task(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True)
    # category
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True ) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title