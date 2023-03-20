from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout
from ..models import User


class SignUpView(TemplateView):
    template_name = "opwork/registration/register.html"

class ProfileView(TemplateView):
    template_name = "opwork/auth/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context["user"] = User.objects.get(pk=user_id)
        return context
    
def logout_view(request):
    logout(request)
    return redirect('home')