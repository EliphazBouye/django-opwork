from django.views.generic.edit import FormView
from .forms import FreelanceForm, UserForm

# Create your views here.
class FreelanceRegisterFormView(FormView):
    template_name = 'freelancer/register.html'
    form_class = FreelanceForm
    success_url = '/freelance/'

    def form_valid(self, form):
        print(form);

# def index(request):
#     context = {
#         'user_form': UserForm,
#         'freelance_form': FreelanceForm,
#     }
#     return render(request, 'freelancer/register.html',context)