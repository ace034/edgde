from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from accounts.models import Account, Settings


class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Account
        fields = ('first_name', 'last_name', 'username', 'email', 'birthday', 'image')


class AccountCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email', 'birthday',)


class AccountAdmin(UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday', 'points', 'image')}),
    )

admin.site.register(Account, AccountAdmin)
admin.site.register(Settings)
