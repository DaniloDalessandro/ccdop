from django import forms
from .models import Colaborador,CentroDeCustoGestor,CentroDeCustoSolicitante,Direcao,Gerencia,Coordenacao,OrcamentoExterno,Orcamento


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

# =========================================================================================================================

from django import forms
from .models import Orcamento, OrcamentoExterno

class OrcamentoForm(forms.ModelForm):
    valores_adicionados = forms.DecimalField(label='Valores Adicionados', max_digits=10, decimal_places=2, required=False, disabled=True)
    valores_enviados = forms.DecimalField(label='Valores Enviados', max_digits=10, decimal_places=2, required=False, disabled=True)
    valor_total = forms.DecimalField(label='Valor Total', max_digits=10, decimal_places=2, required=False, disabled=True)
    orcamento_total = forms.DecimalField(label='Orçamento Total', max_digits=10, decimal_places=2, required=False, disabled=True)

    class Meta:
        model = Orcamento
        fields = ['ano', 'centro', 'classe', 'valor', 'valores_adicionados', 'valores_enviados', 'valor_total', 'orcamento_total']

    def __init__(self, *args, **kwargs):
        super(OrcamentoForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['valores_adicionados'].initial = self.instance.valores_adicionados
            self.fields['valores_enviados'].initial = self.instance.valores_enviados
            self.fields['valor_total'].initial = self.instance.valor_total
            self.fields['orcamento_total'].initial = self.instance.orcamento_total

# =========================================================================================================================

class OrcamentoExternoForm(forms.ModelForm):
    class Meta:
        model = OrcamentoExterno
        fields = ['ano', 'valor', 'centro', 'classe', 'tipo_movimentacao']




