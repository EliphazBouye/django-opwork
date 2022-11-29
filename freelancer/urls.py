from django.urls import path

from .views import FreelanceRegisterFormView

urlpatterns = [
    # path('', )
    path('register/', FreelanceRegisterFormView.as_view(), name="register-freelance"),
]
