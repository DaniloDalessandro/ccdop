from django import forms
from .models import Colaborador,CentroDeCustoGestor,CentroDeCustoSolicitante,Direcao,Gerencia,Coordenacao

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

# =========================================================================================================================

class CentroDeCustoGestorForm(forms.ModelForm):
    class Meta:
        model = CentroDeCustoGestor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'nome': 'Nome',
        }

# =========================================================================================================================

class CentroDeCustoSolicitanteForm(forms.ModelForm):
    class Meta:
        model = CentroDeCustoSolicitante
        fields = ['centro_gestor', 'nome']
        widgets = {
            'centro_gestor': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'centro_gestor': 'Centro Gestor',
            'nome': 'Nome',
        }

# =========================================================================================================================

class DirecaoForm(forms.ModelForm):
    class Meta:
        model = Direcao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'nome': 'Nome',
        }

# =========================================================================================================================

class GerenciaForm(forms.ModelForm):
    class Meta:
        model = Gerencia
        fields = ['direcao', 'nome']
        widgets = {
            'direcao': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'direcao': 'Direção',
            'nome': 'Nome',
        }

# =========================================================================================================================

class CoordenacaoForm(forms.ModelForm):
    class Meta:
        model = Coordenacao
        fields = ['gerencia', 'nome']
        widgets = {
            'gerencia': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
        labels = {
            'gerencia': 'Gerência',
            'nome': 'Nome',
        }

# =========================================================================================================================

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome_completo', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'email']