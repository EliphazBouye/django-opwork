from django.urls import path
from django.views.generic import TemplateView
# from .views import

urlpatterns = [
    # path('', )
    path('', TemplateView.as_view(template_name="opwork/index.html"), name="home"),
    # path('accounts/signup/freelance', )
    # path('register/', FreelanceRegisterFormView.as_view(), name="register-freelance"),
]
