from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Horse

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class HorseForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['name', 'breed', 'age']
