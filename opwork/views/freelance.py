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
    template_name = 'opwork/registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_type"] = 'freelance'
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('freelance_profile')

# @login_required
class FreelanceProfileView(TemplateView):
    template_name = "opwork/auth/profile.html"
    model = Freelance
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context["user"] = User.objects.get(pk=user_id)
        return context
    