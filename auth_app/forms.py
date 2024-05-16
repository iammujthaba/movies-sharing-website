from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class CustomUserChangeForm(UserChangeForm):
    new_password = forms.CharField(label='New Password', max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
