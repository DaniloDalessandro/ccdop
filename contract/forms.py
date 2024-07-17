from django import forms
from .models import Colaborador

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'email']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'mat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'direcao': forms.Select(attrs={'class': 'form-control'}),
            'gerencia': forms.Select(attrs={'class': 'form-control'}),
            'coordenacao': forms.Select(attrs={'class': 'form-control'}),
            'ramal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ramal'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        labels = {
            'nome_completo': 'Nome Completo',
            'mat': 'Matrícula',
            'direcao': 'Direção',
            'gerencia': 'Gerência',
            'coordenacao': 'Coordenação',
            'ramal': 'Ramal',
            'email': 'Email',
        }
        help_texts = {
            'nome_completo': 'Digite o nome completo do colaborador',
            'mat': 'Digite o número de matrícula do colaborador',
            'ramal': 'Digite o ramal de contato',
            'email': 'Digite o endereço de email',
        }
