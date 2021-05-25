from events import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    branch= forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email','branch', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    branch= forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email','branch']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image']

