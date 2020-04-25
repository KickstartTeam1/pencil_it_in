from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from apps.accounts.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        )

