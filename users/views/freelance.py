from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from ..models import Freelance

from ..forms import FreelanceSignUpForm
from ..models import User


class FreelanceSignUpView(CreateView):
    model = User
    form_class = FreelanceSignUpForm
    template_name = 'registration/signup_form.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = 'freelance'
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

# @login_required

    