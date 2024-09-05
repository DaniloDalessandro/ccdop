from django import forms
from .models import AuxilioColaborador

class AuxilioColaboradorForm(forms.ModelForm):
    class Meta:
        model = AuxilioColaborador
        fields = [
            'beneficiado', 'orcamento', 'tipo', 'beneficio',
            'valor_parcela', 'qtd_parcelas', 'obs', 'mes_inicio'
        ]
        widgets = {
            'beneficiado': forms.Select(attrs={'class': 'form-control'}),  # Campo de seleção para o colaborador
            'orcamento': forms.Select(attrs={'class': 'form-control'}),  # Campo de seleção para o orçamento
            'tipo': forms.Select(attrs={'class': 'form-control'}),  # Campo de seleção para o tipo de auxílio
            'beneficio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o benefício'}),  # Campo de texto para o benefício
            'valor_parcela': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor da parcela'}),  # Campo numérico para valor por parcela
            'qtd_parcelas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de parcelas'}),  # Campo numérico para quantidade de parcelas
            'obs': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observações (opcional)'}),  # Campo de texto para observações
            'mes_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # Campo de data com seletor de calendário
        }

    def clean(self):
        cleaned_data = super().clean()
        valor_parcela = cleaned_data.get("valor_parcela")
        qtd_parcelas = cleaned_data.get("qtd_parcelas")

        # Verificação básica: valor_parcela e qtd_parcelas devem ser positivos
        if valor_parcela is not None and valor_parcela <= 0:
            self.add_error('valor_parcela', 'O valor da parcela deve ser positivo.')

        if qtd_parcelas is not None and qtd_parcelas <= 0:
            self.add_error('qtd_parcelas', 'A quantidade de parcelas deve ser positiva.')

        return cleaned_data
