"""upwork_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from opwork.views import opwork, freelance, client

urlpatterns = [
    path('', include('opwork.urls')),
    path('account/signup/', opwork.SignUpView.as_view(), name="signup"),
    path('account/signup/freelance/', freelance.FreelanceSignUpView.as_view(), name="freelance_signup"),
    path('account/signup/client/', client.ClientSignUpView.as_view(), name="client_signup"),
    path('admin/', admin.site.urls),
]
