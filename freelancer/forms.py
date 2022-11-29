from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, forms
from .models import Freelance

class FreelanceForm(UserCreationForm):
    
    bio = forms.CharField(widget=forms.Textarea(attrs={'name': 'bio', 'row': 30, 'cols': 30}))
    class Meta:
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        model = get_user_model()
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        
        Freelance.objects.create(user=user, bio=self.cleaned_data.get("bio"))
        return user