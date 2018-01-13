from django.urls import path, include
from django.contrib.auth.views import LoginView

from .views import RegistrationView

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', RegistrationView.as_view(), name='register'),
]
