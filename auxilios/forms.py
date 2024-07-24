from django import forms
from .models import AuxilioColaborador

class AuxilioColaboradorForm(forms.ModelForm):
    class Meta:
        model = AuxilioColaborador
        fields = [
            'baneficiado',
            'orcamento',
            'tipo',
            'valor_parcela',
            'qtd_parcelas',
            'obs',
            'mes_inicio',
        ]
        labels = {
            'baneficiado': 'Beneficiado',
            'orcamento': 'Orçamento',
            'tipo': 'Tipo de Auxílio',
            'valor_parcela': 'Valor por Parcela',
            'qtd_parcelas': 'Quantidade de Parcelas',
            'obs': 'Observações',
            'mes_inicio': 'Mês de Início',
        }
        widgets = {
            'mes_inicio': forms.DateInput(attrs={'type': 'date'}),
        }
