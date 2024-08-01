from django import forms
from .models import Colaborador,CentroDeCustoGestor,CentroDeCustoSolicitante,Direcao,Gerencia,Coordenacao,OrcamentoExterno,Orcamento,LinhaOrcamentaria,Contrato
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
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'mat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'direcao': forms.Select(attrs={'class': 'form-control'}),
            'gerencia': forms.Select(attrs={'class': 'form-control'}),
            'coordenacao': forms.Select(attrs={'class': 'form-control'}),
            'ramal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ramal'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

# =========================================================================================================================
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

# =========================================================================================================================

from .models import LinhaOrcamentaria

class LinhaOrcamentariaForm(forms.ModelForm):
    class Meta:
        model = LinhaOrcamentaria
        fields = [
            'classe',
            'custo_despesa',
            'centro_custo_gestor',
            'centro_custo_solicitante',
            'descricao_resumida',
            'objeto',
            'classificacao_orcamento',
            'possivel_fiscal',
            'ano_orcamento',
            'tipo_contrato',
            'status_linha_orcamentaria',
            'tipo_provavel_contratacao',
            'valor_orcado',
            'status_elaboracao_tr',
            'necessidade_contratacao',
            'status_processo',
            'status_contratacao',
            'obs_contrato',
        ]
        widgets = {
            'descricao_resumida': forms.TextInput(attrs={'class': 'form-control'}),
            'objeto': forms.Textarea(attrs={'class': 'form-control'}),
            'obs_contrato': forms.Textarea(attrs={'class': 'form-control'}),
            'valor_orcado': forms.NumberInput(attrs={'class': 'form-control'}),
            'necessidade_contratacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # Adicione outros widgets personalizados conforme necessário
        }


class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = [
            'linha_orcamentaria',
            'data_assinatura',
            'data_vencimento',
            'fical_principal',
            'fical_substituto',
            'valor_contrato'
        ]
        widgets = {
            'data_assinatura': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_vencimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'linha_orcamentaria': forms.Select(attrs={'class': 'form-control'}),
            'fical_principal': forms.Select(attrs={'class': 'form-control'}),
            'fical_substituto': forms.Select(attrs={'class': 'form-control'}),
            'valor_contrato': forms.NumberInput(attrs={'class': 'form-control'}),
        }
