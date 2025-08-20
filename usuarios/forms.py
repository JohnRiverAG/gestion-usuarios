

# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario # Si usas modelo personalizado

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario # Si usas modelo personalizado
        fields = ['username', 'email', 'telefono', 'password']

class LoginForm(AuthenticationForm):
    pass
