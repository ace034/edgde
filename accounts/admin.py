from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from accounts.models import Account, Settings


class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Account
        fields = ('first_name', 'last_name', 'username', 'email', 'birthday')


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email', 'birthday', 'password', 'password1')


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday', 'points')}),
    )

admin.site.register(Account, AccountAdmin)
admin.site.register(Settings)
