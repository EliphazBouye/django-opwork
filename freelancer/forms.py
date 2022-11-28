from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Freelance

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
    


class FreelanceForm(ModelForm):
    
    class Meta:
        model = Freelance
        fields = ['bio']
