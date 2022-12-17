from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import fields
from django.forms.forms import Form
from .models import *

from django.contrib.auth.models import User  #agregado
from django.contrib.auth import password_validation #agregado

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'resumen', 'texto', 'imagen', 'categoria', 'usuario']


class RegistroForm(UserCreationForm):
    """email = forms.EmailField(max_length=50, help_text='',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))"""
    password1 = forms.CharField(label=('Contraseña'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=('Confirmar contraseña'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=(''))
    username = forms.CharField(
        label=('Nombre de usuario'),
        max_length=150,
        help_text=(''),
        error_messages={'unique': ("El nombre de usuario ya existe.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)