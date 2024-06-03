from django.db import models
from datetime import datetime

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    mat = models.IntegerField(null=True, blank=True,verbose_name='Matrícula')
    cargo = models.CharField(max_length=50)
    fone = models.CharField(max_length=11,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.nome_completo
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

class Orcamento(models.Model):
    ano = models.IntegerField(unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.ano)
    
    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
    
class CentroDeCusto(models.Model):
        
    centro_gestor = models.CharField(max_length=20)
    centro_solicitante = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.centro_gestor} - {self.centro_solicitante}"
  
class Contrato(models.Model):
    CLASSE_CHOICES = [
        ('I', 'OPEX'),
        ('II', 'CAPEX'),        
    ]
    
    classe = models.CharField(max_length=100,choices=CLASSE_CHOICES,blank='true',null='true')
    CUSTODESPESA_CHOICES = [
        ('I', 'Base Principal'),
        ('II', 'Serviços Especializados'),
        ('III','Despesas Compartilhadas'), 
        ('IV','Máquinas e Equipamentos'),
        ('V','Equip. de Informática'), 
        ('VI','Software e Licenças'),   
    ]
    custo_despesa = models.CharField(max_length=100,choices=CUSTODESPESA_CHOICES,default='I')
    centro_custo = models.ForeignKey('CentroDeCusto', on_delete=models.PROTECT, related_name='contratos', null=True, blank=True)
    descricao_resumida = models.CharField(max_length=255, null=True)
    CLASSIFICACAO_CHOICES = [
        ('NOVO', 'NOVO'),
        ('RENOVAÇÃO', 'RENOVAÇÃO'),
        ('CARY OVER', 'CARY OVER'),
        ('REPLANEJAMENTO', 'REPLANEJAMENTO'),
    ]
    classificacao_orcamento = models.CharField(max_length=100,choices=CLASSIFICACAO_CHOICES,null=True, blank=True)
    fiscal_principal = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='contratos_fiscal_principal')
    fiscal_substituto = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='contratos_fiscal_substituto', null=True, blank=True)
    ano_orcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT, related_name='contratos', null=True, blank=True)
    STATUSPROCESSO_CHOICES = [
        ('I', 'PLANEJAMENTO'),
        ('II', 'Execução'),
        ('III','Elaboração de TR'), 
        ('IV','Cotação'),
        ('V','Em proc. aditivo'),           
    ]
    status_processo = models.CharField(max_length=100,choices=STATUSPROCESSO_CHOICES,blank=True,null=True)
    TIPOCONTRATO_CHOICES = [
        ('I', 'SERVIÇO'),
        ('II', 'FORNECIMENTO'),
        ('III','ASSINATURA'), 
        ('IV','FORNECIMENTO/SERVIÇO'),                 
    ]
    tipo_contrato = models.CharField(max_length=100,choices=TIPOCONTRATO_CHOICES,blank=True,null=True)
    TIPOCONTRATACAOPROVAVEL_CHOICES = [
        ('I', 'LICITAÇÃO'),
        ('II', 'DISPENSA EM RAZÃO DO VALOR'),
        ('IV','CONVÊNIO'),  
        ('V','FUNDO FIXO'),  
        ('VI','INEXIGIBILIDADE'),                 
    ]
    valor_orcado = models.FloatField(default=0,blank=True,null=True)
    remanejamento = models.FloatField(default=0,blank=True,null=True)
    mes_referencia = models.CharField(max_length=7,blank=True,null=True)
    data_prevista_tr = models.DateField(blank=True,null=True)
    STATUSELABORACAOTR_CHOICES = [
        ('I', 'VENCIDO'),
        ('II', 'DENTRO DO PRAZO'),
        ('III','ELABORADO COM ATRAZO'), 
        ('IV','ELABORADO NO PRAZO'),  
    ]
    status_elaboracao_tr = models.CharField(max_length=100,choices=STATUSELABORACAOTR_CHOICES,blank=True,null=True)

    obs_contrato = models.TextField(max_length=400,blank=True,null=True)
    necessidade_contratacao = models.CharField(max_length=7,blank=True,null=True)
    STATUSCONTRATACAO_CHOICES = [
        ('I', 'DENTRO DO PRAZO'),
        ('II', 'CONTRATADO'),
        ('III','VENCIDO'),        
    ]
    status_contratacao = models.CharField(max_length=100,choices=STATUSCONTRATACAO_CHOICES,blank=True,null=True)

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
    
    def __str__(self):
        return self.descricao_resumida
    
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
    valor = models.FloatField(blank=True,null=True)
    diretoria = models.CharField(max_length=100, blank=True,null=True)
    centro_custo = models.CharField(max_length=100,blank=True,null=True)