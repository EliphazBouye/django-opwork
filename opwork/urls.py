from django.urls import path
from django.views.generic import TemplateView
# from .views import
from django.contrib.auth import views as auth_login
urlpatterns = [
    # path('', )
    path('', TemplateView.as_view(template_name="opwork/index.html"), name="home"),
    path('accounts/login/', auth_login.LoginView.as_view(template_name="opwork/registration/login.html"))
    # path('accounts/signup/freelance', )
    # path('register/', FreelanceRegisterFormView.as_view(), name="register-freelance"),
]
