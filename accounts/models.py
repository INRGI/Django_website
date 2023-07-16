from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=20)
    pesel = models.CharField(max_length=11, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def get_username(self):
        return self.username


class Pit(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='pits')
    file = models.FileField(upload_to='pits/')

    def __str__(self):
        return self.file.name
