from django import forms
from .models import AuxilioColaborador

class AuxilioColaboradorForm(forms.ModelForm):
    class Meta:
        model = AuxilioColaborador
        fields = [
            'baneficiado', 'orcamento', 'tipo', 'beneficio',
            'valor_parcela', 'qtd_parcelas', 'obs', 'mes_inicio'
        ]
        widgets = {
            'baneficiado': forms.Select(attrs={'class': 'form-control'}),
            'orcamento': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'beneficio': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_parcela': forms.NumberInput(attrs={'class': 'form-control'}),
            'qtd_parcelas': forms.NumberInput(attrs={'class': 'form-control'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mes_inicio': forms.Select(attrs={'class': 'form-select'}),
        }
