from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, forms
from .models import Freelance, Client

class FreelanceSignUpForm(UserCreationForm):
    class Meta:
        fields = ['first_name', 'last_name','username', 'email']
        model = get_user_model()
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
    def save(self):
        user = super().save(commit=False)
        user.is_freelance = True
        user.save()
        Freelance.objects.create(user=user)
        return user


class ClientSignUpForm(UserCreationForm):
    class Meta:
        fields = ['first_name', 'last_name','username', 'email']
        model = get_user_model()
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        Client.objects.create(user=user)
        return user
    
