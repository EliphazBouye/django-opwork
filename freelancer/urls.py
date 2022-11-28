from django.urls import path

from .views import FreelanceRegisterFormView

urlpatterns = [
    path('', FreelanceRegisterFormView.as_view(), name="register-freelance"),
]
