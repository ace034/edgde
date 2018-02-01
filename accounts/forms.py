from django.forms import ModelForm

from .models import Account


class EditProfileForm(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'image']
