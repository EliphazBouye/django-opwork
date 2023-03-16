from django.views.generic import CreateView
from .forms import FreelanceForm
from django.urls import reverse_lazy

# Create your views here.
class FreelanceRegisterFormView(CreateView):
    template_name = 'opwork/register.html'
    form_class = FreelanceForm
    success_url = reverse_lazy("opwork:index")
