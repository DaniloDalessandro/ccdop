from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'email')

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'email')
