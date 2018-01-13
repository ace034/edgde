from django.shortcuts import render
from django.views import View

from .admin import AccountCreationForm

class RegistrationView(View):
    template_name = 'registration/register.html'
    form_class = AccountCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
