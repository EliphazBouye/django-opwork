from django.db import models
from django.contrib.auth.models import AbstractUser

class Freelance(AbstractUser):
    username = models.CharField(
        verbose_name='unique username',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(
        verbose_name='first name',
        max_length=255,
        unique=True
    )
    last_name = models.CharField(
        verbose_name='last name',
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    address = models.CharField(
        verbose_name='location address',
        max_length=255,
    )
    bio = models.TextField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email']
    
    def __str__(self):
        return self.username
    