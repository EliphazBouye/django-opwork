from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    is_freelance = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    bio = models.TextField()

class Freelance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user")

    def __str__(self):
        return self.username
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.firstname
 