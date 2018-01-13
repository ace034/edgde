from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from accounts.models import Account, Settings


class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Account


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday', 'points')}),
    )

admin.site.register(Account, AccountAdmin)
admin.site.register(Settings)
