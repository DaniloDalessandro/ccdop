from django.db import models
from datetime import datetime
from decimal import Decimal
from collaborator.models import Colaborador

class Orcamento(models.Model):
    ano = models.IntegerField(unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    CENTRO = [
        ('I', 'DOP'),
        ('II', 'GELOG'),
        ('III', 'GESAS'), 
        ('IV', 'GESAS'),          
    ]
    centro = models.CharField(max_length=100,choices=CENTRO,unique=True)

    def __str__(self):
        return str(self.ano)
    
    @property
    def valor_adicionado(self):
        soma_externo = OrcamentoExterno.objects.filter(ano=self, is_deduction=False).aggregate(total=models.Sum('valor'))['total'] or 0
        return Decimal(soma_externo)

    @property
    def valor_subtraido(self):
        deducao_externo = OrcamentoExterno.objects.filter(ano=self, is_deduction=True).aggregate(total=models.Sum('valor'))['total'] or 0
        return Decimal(deducao_externo)
    
    @property
    def valor_total(self):
        valor_externo = OrcamentoExterno.objects.filter(ano=self).aggregate(total=models.Sum('valor'))['total'] or 0
        return self.valor + Decimal(valor_externo)
    
    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
    
class CentroDeCusto(models.Model):
        
    centro_gestor = models.CharField(max_length=20)
    centro_solicitante = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.centro_gestor} - {self.centro_solicitante}"
  
from django.db import models
from datetime import datetime

class Contrato(models.Model):
    CLASSE_CHOICES = [
        ('I', 'OPEX'),
        ('II', 'CAPEX'),        
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)

    CUSTODESPESA_CHOICES = [
        ('I', 'Base Principal'),
        ('II', 'Serviços Especializados'),
        ('III', 'Despesas Compartilhadas'), 
        ('IV', 'Máquinas e Equipamentos'),
        ('V', 'Equip. de Informática'), 
        ('VI', 'Software e Licenças'),   
    ]
    custo_despesa = models.CharField(max_length=100, choices=CUSTODESPESA_CHOICES, default='I')

    centro_custo = models.ForeignKey('CentroDeCusto', on_delete=models.PROTECT, related_name='contratos', null=True, blank=True)
    descricao_resumida = models.CharField(max_length=255, null=True, blank=True)

    CLASSIFICACAO_CHOICES = [
        ('NOVO', 'NOVO'),
        ('RENOVAÇÃO', 'RENOVAÇÃO'),
        ('CARY OVER', 'CARY OVER'),
        ('REPLANEJAMENTO', 'REPLANEJAMENTO'),
    ]
    classificacao_orcamento = models.CharField(max_length=100, choices=CLASSIFICACAO_CHOICES, null=True, blank=True)

    fiscal_principal = models.ForeignKey('colaborador', on_delete=models.PROTECT, related_name='contratos_fiscal_principal')
    fiscal_substituto = models.ForeignKey('colaborador', on_delete=models.PROTECT, related_name='contratos_fiscal_substituto', null=True, blank=True)

    ano_orcamento = models.ForeignKey('Orcamento', on_delete=models.PROTECT, related_name='contratos', null=True, blank=True)

    STATUSPROCESSO_CHOICES = [
        ('I', 'PLANEJAMENTO'),
        ('II', 'Execução'),
        ('III', 'Elaboração de TR'), 
        ('IV', 'Cotação'),
        ('V', 'Em proc. aditivo'),           
    ]
    status_processo = models.CharField(max_length=100, choices=STATUSPROCESSO_CHOICES, blank=True, null=True)

    TIPOCONTRATO_CHOICES = [
        ('I', 'SERVIÇO'),
        ('II', 'FORNECIMENTO'),
        ('III', 'ASSINATURA'), 
        ('IV', 'FORNECIMENTO/SERVIÇO'),                 
    ]
    tipo_contrato = models.CharField(max_length=100, choices=TIPOCONTRATO_CHOICES, blank=True, null=True)

    TIPOCONTRATACAOPROVAVEL_CHOICES = [
        ('I', 'LICITAÇÃO'),
        ('II', 'DISPENSA EM RAZÃO DO VALOR'),
        ('IV', 'CONVÊNIO'),  
        ('V', 'FUNDO FIXO'),  
        ('VI', 'INEXIGIBILIDADE'),                 
    ]
    valor_orcado = models.FloatField(default=0, blank=True, null=True)
    valor_utilizado = models.FloatField(default=0, blank=True, null=True)  # Campo para valor utilizado
    remanejamento = models.FloatField(default=0, blank=True, null=True)
    mes_referencia = models.CharField(max_length=7, blank=True, null=True)
    data_prevista_tr = models.DateField(blank=True, null=True)

    STATUSELABORACAOTR_CHOICES = [
        ('I', 'VENCIDO'),
        ('II', 'DENTRO DO PRAZO'),
        ('III', 'ELABORADO COM ATRASO'), 
        ('IV', 'ELABORADO NO PRAZO'),  
    ]
    status_elaboracao_tr = models.CharField(max_length=100, choices=STATUSELABORACAOTR_CHOICES, blank=True, null=True)

    obs_contrato = models.TextField(max_length=400, blank=True, null=True)
    necessidade_contratacao = models.DateField(blank=True, null=True)

    STATUSCONTRATACAO_CHOICES = [
        ('I', 'DENTRO DO PRAZO'),
        ('II', 'CONTRATADO'),
        ('III', 'VENCIDO'),        
    ]
    status_contratacao = models.CharField(max_length=100, choices=STATUSCONTRATACAO_CHOICES, blank=True, null=True)

    @property
    def aviso_fiscal(self):
        if self.necessidade_contratacao:
            delta = datetime.now().date() - self.necessidade_contratacao
            dias_restantes = max(150 - delta.days, 0)
            return f"{dias_restantes} dias"
        return "150 dias"

    @property
    def elaboracao_tr(self):
        if self.necessidade_contratacao:
            delta = datetime.now().date() - self.necessidade_contratacao
            dias_restantes = max(110 - delta.days, 0)
            return f"{dias_restantes} dias"
        return "110 dias"

    @property
    def abertura_tr(self):
        if self.necessidade_contratacao:
            delta = datetime.now().date() - self.necessidade_contratacao
            dias_restantes = max(90 - delta.days, 0)
            return f"{dias_restantes} dias"
        return "90 dias"

    @property
    def percentual_utilizacao(self):
        if self.valor_orcado > 0:
            percentual = (self.valor_utilizado / self.valor_orcado) * 100
            return f"{percentual:.2f}%"
        return "0.00%"

    def __str__(self):
        return self.descricao_resumida or "Contrato sem descrição"

    class Meta:
        verbose_name = 'Linha Orçamentaria'
        verbose_name_plural = 'Linhas Orçamentarias'


class Aditivo(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.PROTECT, related_name='aditivos')
    data_aditivo = models.DateField()
    descricao = models.TextField(max_length=500, blank=True, null=True)
    novo_prazo = models.DateField(blank=True, null=True)
    novo_valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class OrcamentoExterno(models.Model):
    ano = models.ForeignKey(Orcamento,on_delete=models.PROTECT)
    is_deduction = models.BooleanField(default=False,verbose_name='Retirada de orçamento')
    valor = models.FloatField(blank=True,null=True)
    diretoria = models.CharField(max_length=100, blank=True,null=True)
    centro_custo = models.CharField(max_length=100,blank=True,null=True)