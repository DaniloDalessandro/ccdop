from django.db import models
from contract.models import Colaborador,Orcamento
from django.db.models import F
from datetime import date
from dateutil.relativedelta import relativedelta # type: ignore

# Create your models here.

class AuxilioColaborador(models.Model):
    baneficiado = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    orcamento = models.ForeignKey(Orcamento, related_name='auxilios_colaboradores', on_delete=models.PROTECT)
    tipo_choices = [
        ('A', 'Graduação'),
        ('B', 'Pós-Graduação'),
        ('C', 'Auxilio creche escola'),
    ]
    tipo = models.CharField(max_length=100, choices=tipo_choices, null=True, blank=True)
    valor_parcela = models.FloatField(null=True, blank=True)
    valor_total = models.FloatField(null=True, blank=True, editable=False)
    obs = models.CharField(max_length=200, null=True, blank=True)
    mes_inicio = models.DateField()
    qtd_parcelas = models.PositiveIntegerField()
    mes_fim = models.DateField(editable=False)

    @property
    def valor_total_auxilios(self):
        total_auxilios = AuxilioColaborador.objects.aggregate(total=Sum('valor_total'))['total']
        return total_auxilios or 0

    def save(self, *args, **kwargs):
        # Calcular valor_total como a soma de todas as parcelas
        if self.valor_parcela and self.qtd_parcelas:
            self.valor_total = self.valor_parcela * self.qtd_parcelas
        
        # Calcular mes_fim com base em mes_inicio e qtd_parcelas
        if self.mes_inicio and self.qtd_parcelas:
            mes_fim_date = self.mes_inicio + relativedelta(months=self.qtd_parcelas)
            self.mes_fim = mes_fim_date

        if not self.pk:
            # Novo objeto, subtrai o valor do orçamento
            self.orcamento.valor = F('valor') - self.valor_total
        else:
            # Objeto existente, ajustar orçamento
            old_instance = AuxilioColaborador.objects.get(pk=self.pk)
            # Revertendo o efeito da instância antiga e aplicando o da nova instância
            self.orcamento.valor = F('valor') + old_instance.valor_total - self.valor_total
        
        self.orcamento.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.orcamento:
            # Reverter o valor do orçamento ao deletar
            self.orcamento.valor = F('valor') + self.valor_total
            self.orcamento.save()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Auxílio Colaborador'
        verbose_name_plural = 'Auxílios Colaboradores'