from django.urls import path, include
from django.views.generic import TemplateView
from .views import users, freelance, client
from django.contrib.auth import views as auth_login
urlpatterns = [
    # path('', )
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', users.SignUpView.as_view(), name="signup"),
    # path('account/login/', users.SignInView.as_view(), name="login"),
    path('accounts/signup/freelance/', freelance.FreelanceSignUpView.as_view(), name="freelance_signup"),
    path('accounts/signup/client/', client.ClientSignUpView.as_view(), name="client_signup"),
    path('accounts/profile/', users.ProfileView.as_view(), name="profile"),
    path('logout/', users.logout, name="logout"),
]
