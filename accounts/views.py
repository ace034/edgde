from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from .admin import AccountCreationForm
from .forms import EditProfileForm


class RegistrationView(View):
    template_name = 'registration/register.html'
    form_class = AccountCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)

            return redirect('accounts:profile')

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    template_name = 'registration/edit_profile.html'
    form_class = EditProfileForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('accounts:profile')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'registration/profile.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
