from django.urls import path, include
from django.views.generic import TemplateView
from .views import users, freelance, client
from django.contrib.auth import views as auth_login
urlpatterns = [
    # path('', )
    path('accounts/signup/', users.SignUpView.as_view(), name="signup"),
    path('accounts/login/', auth_login.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('accounts/signup/freelance/', freelance.FreelanceSignUpView.as_view(), name="freelance_signup"),
    path('accounts/signup/client/', client.ClientSignUpView.as_view(), name="client_signup"),
    path('accounts/password-reset/', auth_login.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="password_reset"),
    path('accounts/password-change/', auth_login.PasswordChangeView.as_view(), name="password_change"),
    path('accounts/password-change/done/', auth_login.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/', auth_login.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/password-reset/complete/', auth_login.PasswordResetCompleteView.as_view(template_name="registration/password_change_completed.html"), name="password_reset_complete"),
    path('accounts/profile/', users.ProfileView.as_view(template_name="users/auth/profile.html"), name="profile"),
    path('logout/', users.logout_view, name="logout"),
]
