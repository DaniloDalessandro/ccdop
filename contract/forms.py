from django import forms
from .models import (Colaborador,CentroDeCustoGestor,CentroDeCustoSolicitante,Direcao,Gerencia,Coordenacao,
                     OrcamentoExterno,Orcamento,LinhaOrcamentaria,Contrato,Remanejamento,Aditivo,Prestacao)

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

    def __init__(self, *args, **kwargs):
        super(ColaboradorForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


# =========================================================================================================================

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
        fields = ['ano', 'centro', 'classe', 'valor', 'tipo_movimentacao']

    def __init__(self, *args, **kwargs):
        super(OrcamentoExternoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


# =========================================================================================================================

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

# =========================================================================================================================

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = [
            'linha_orcamentaria',
            'data_assinatura',
            'data_vencimento',
            'fiscal_principal',
            'fiscal_substituto',
            'valor_contrato',
        ]
        widgets = {
            'data_assinatura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_vencimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'linha_orcamentaria': forms.Select(attrs={'class': 'form-select'}),
            'fiscal_principal': forms.Select(attrs={'class': 'form-select'}),
            'fiscal_substituto': forms.Select(attrs={'class': 'form-select'}),
            'valor_contrato': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# =========================================================================================================================

class PrestacaoForm(forms.ModelForm):
    class Meta:
        model = Prestacao
        fields = ['data_vencimento', 'data_pagamento', 'status_pagamento']
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_pagamento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status_pagamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# =========================================================================================================================

class RemanejamentoForm(forms.ModelForm):
    class Meta:
        model = Remanejamento
        fields = [
            'valor',
            'linha_origem',
            'linha_destino',
            'motivo',
        ]
        widgets = {
            'linha_origem': forms.Select(attrs={'class': 'form-control'}),
            'linha_destino': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control'}),
        }

# =========================================================================================================================

class AditivoForm(forms.ModelForm):
    class Meta:
        model = Aditivo
        fields = ['contrato', 'data', 'valor', 'justificativa']
        widgets = {
            'contrato': forms.Select(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'justificativa': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'contrato': 'Contrato',
            'data': 'Data do Aditivo',
            'valor': 'Valor do Aditivo',
            'justificativa': 'Justificativa',
        }

# =========================================================================================================================

class CentroDeCustoGestorForm(forms.ModelForm):
    class Meta:
        model = CentroDeCustoGestor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Centro de Custo Gestor'}),
        }


# =========================================================================================================================

class CentroDeCustoSolicitanteForm(forms.ModelForm):
    class Meta:
        model = CentroDeCustoSolicitante
        fields = ['centro_gestor', 'nome']
        widgets = {
            'centro_gestor': forms.Select(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Centro de Custo Solicitante'}),
        }
