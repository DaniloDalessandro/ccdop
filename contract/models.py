from django.db import models
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal
from django.utils import timezone

# ============================================================================================================

class CentroDeCustoGestor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
# ============================================================================================================

class CentroDeCustoSolicitante(models.Model):
    centro_gestor = models.ForeignKey(CentroDeCustoGestor, on_delete=models.CASCADE, related_name='solicitantes')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        unique_together = ('centro_gestor', 'nome')
    
# ============================================================================================================

class Setores(models.Model):
    diretoria = models.CharField(max_length=10)
    gerencia = models.CharField(max_length=10)
    setor = models.CharField(max_length=100,verbose_name='Setor',unique=True)

    def __str__(self):
        return f"{self.gerencia} - {self.setor}"
    
    class Meta:
        unique_together = ('diretoria','gerencia','setor')

# ============================================================================================================

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    mat = models.IntegerField(null=True, blank=True,verbose_name='Matrícula')     
    setor = models.ForeignKey(Setores,on_delete=models.CASCADE,to_field='setor')
    ramal = models.CharField(max_length=4,null=True, blank=True)
    email = models.EmailField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.nome_completo
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

# ============================================================================================================

class Orcamento(models.Model):
    ano = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2,default=Decimal('0.00'))
    valor_adicionado = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), editable=False)
    valor_subtraido = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), editable=False)
    
    centro = models.ForeignKey(CentroDeCustoGestor,on_delete=models.CASCADE)
    CLASSE_CHOICES = [
        ('A', 'OPEX'),
        ('B', 'CAPEX'),        
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.ano} - {self.centro}"
            
    @property
    def valor_total(self):
        return self.valor + self.valor_adicionado - self.valor_subtraido
    
    @property
    def orcamento_dop_geral(self):
        total_orcamento_centros = Orcamento.objects.filter(ano=self.ano).aggregate(total=Sum('valor'))['total'] or 0
        total_valor_externo = OrcamentoExterno.objects.filter(ano__ano=self.ano).aggregate(total=Sum('valor'))['total'] or 0
        return Decimal(total_orcamento_centros) + Decimal(total_valor_externo)

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
        unique_together = ('ano', 'centro', 'classe')

# ============================================================================================================

class OrcamentoExterno(models.Model):
    ano = models.ForeignKey('Orcamento', on_delete=models.CASCADE, related_name='orcamentos_externos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    centro = models.CharField(max_length=20)
    CLASSE_CHOICES = [
        ('OPEX', 'OPEX'),
        ('CAPEX', 'CAPEX'),        
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)
    is_deduction = models.BooleanField(default=False, verbose_name='Envio de Orçamento')

    def __str__(self):
        return f"{self.ano} - {self.centro} - {'Dedução' if self.is_deduction else 'Adição'}"

    class Meta:
        verbose_name = 'Orçamento Externo'
        verbose_name_plural = 'Orçamentos Externos'

# ============================================================================================================

class LinhaOrcamentaria(models.Model):
    CLASSE_CHOICES = [
        ('A', 'OPEX'),
        ('B', 'CAPEX'),        
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)

    CUSTODESPESA_CHOICES = [
        ('A', 'Base Principal'),
        ('B', 'Serviços Especializados'),
        ('C', 'Despesas Compartilhadas'), 
        ('D', 'Máquinas e Equipamentos'),
        ('E', 'Equip. de Informática'), 
        ('F', 'Software e Licenças'),
        ('G', 'Input da Base Principal'),
        ('H', 'Contribuições em Geral'), 
        ('I', 'Locação de Bens e Móveis'),  
        ('J', 'Fardamento e EPI'),
        ('L', 'Assinaturas e Publicações'),     
    ]
    custo_despesa = models.CharField(max_length=100, choices=CUSTODESPESA_CHOICES,verbose_name='CUSTO/DESPESA')

    centro_custo_gestor = models.ForeignKey(CentroDeCustoGestor, on_delete=models.SET_NULL, null=True, blank=True)
    centro_custo_solicitante = models.ForeignKey(CentroDeCustoSolicitante, on_delete=models.SET_NULL, null=True, blank=True)
    descricao_resumida = models.CharField(max_length=255, null=True, blank=True,verbose_name='Finalidade')

    CLASSIFICACAO_CHOICES = [
        ('NOVO', 'NOVO'),
        ('RENOVAÇÃO', 'RENOVAÇÃO'),
        ('CARY OVER', 'CARY OVER'),
        ('REPLANEJAMENTO', 'REPLANEJAMENTO'),
        ('N/A', 'N/A'),
    ]
    classificacao_orcamento = models.CharField(max_length=100, choices=CLASSIFICACAO_CHOICES, null=True, blank=True)

    possivel_fiscal = models.ForeignKey('Colaborador', on_delete=models.PROTECT, related_name='contratos_fiscal_possivel', verbose_name='Fiscal')
    
    ano_orcamento = models.ForeignKey(Orcamento, on_delete=models.PROTECT, related_name='contratos', null=True, blank=True)
 
    TIPOCONTRATO_CHOICES = [
        ('I', 'SERVIÇO'),
        ('II', 'FORNECIMENTO'),
        ('III', 'ASSINATURA'), 
        ('IV', 'FORNECIMENTO/SERVIÇO'),                 
    ]
    tipo_contrato = models.CharField(max_length=100, choices=TIPOCONTRATO_CHOICES, blank=True, null=True)

    TIPOCONTRATACAOPROVAVEL_CHOICES = [
        ('A', 'LICITAÇÃO'),
        ('B', 'DISPENSA EM RAZÃO DO VALOR'),
        ('C', 'CONVÊNIO'),  
        ('D', 'FUNDO FIXO'),  
        ('E', 'INEXIGIBILIDADE'),
        ('F', 'ATA DE REGISTRO DE PREÇO'), 
        ('H', 'ACORDO DE COOPERAÇÃO'), 
        ('I', 'APOSTILAMENTO'),                  
    ]
    tipo_provavel_contratacao = models.CharField(max_length=100,choices=TIPOCONTRATACAOPROVAVEL_CHOICES)
    valor_orcado = models.FloatField(default=0, blank=True, null=True)
           
    STATUSELABORACAOTR_CHOICES = [
        ('I', 'VENCIDO'),
        ('II', 'DENTRO DO PRAZO'),
        ('III', 'ELABORADO COM ATRASO'), 
        ('IV', 'ELABORADO NO PRAZO'),  
    ]
    status_elaboracao_tr = models.CharField(max_length=100, choices=STATUSELABORACAOTR_CHOICES, blank=True, null=True)
    
    necessidade_contratacao = models.DateField(blank=True, null=True)

    STATUSPROCESSO_CHOICES = [
        ('I', 'PLANEJAMENTO'),
        ('II', 'Execução'),
        ('III', 'Elaboração de TR'), 
        ('IV', 'Cotação'),
        ('V', 'Em proc. aditivo'),           
    ]
    status_processo = models.CharField(max_length=100, choices=STATUSPROCESSO_CHOICES, blank=True, null=True)

    STATUSCONTRATACAO_CHOICES = [
        ('A', 'DENTRO DO PRAZO'),
        ('B', 'CONTRATADO NO PRAZO'),
        ('C', 'CONTRATADO COM ATRASO'), 
        ('D', 'PRAZO VENCIDO'),   
        ('E', 'LINHA TOTALMENTE REMANEJADA'),
        ('F', 'LINHA TOTALMENTE EXECUTADA'),   
        ('G', 'LINHA DE PAGAMENTO'),    
        ('H', 'LINHA PARCIALMENTE REMANEJADA'), 
        ('I', 'LINHA PARCIALMENTE EXECUTADA'),  
        ('J', 'N/A'), 
    ]
    status_contratacao = models.CharField(max_length=100, choices=STATUSCONTRATACAO_CHOICES, blank=True, null=True)
    obs_contrato = models.TextField(max_length=400, blank=True, null=True)
    @property
    def percentual_utilizacao(self):
        if self.valor_orcado > 0:
            percentual = (self.valor_utilizado / self.valor_orcado) * 100
            return f"{percentual:.2f}%"
        return "0.00%"
    
    @property
    def valor_remanejado_total(self):
        remanejamentos_origem = self.remanejamentos_origem.aggregate(total=Sum('valor'))['total'] or Decimal(0)
        remanejamentos_destino = self.remanejamentos_destino.aggregate(total=Sum('valor'))['total'] or Decimal(0)
        return remanejamentos_origem + remanejamentos_destino
    
    @property
    def saldo_orcamentario_pos_remanejamento(self):
        valor_remanejado_origem = self.remanejamentos_origem.aggregate(total=Sum('valor'))['total'] or Decimal(0)
        valor_remanejado_destino = self.remanejamentos_destino.aggregate(total=Sum('valor'))['total'] or Decimal(0)
        saldo = self.valor_orcado + valor_remanejado_destino - valor_remanejado_origem - self.valor_utilizado
        return saldo
    
    @property
    def tempo_para_contratacao(self):
        if self.necessidade_contratacao:
            dias_restantes = (self.necessidade_contratacao - datetime.now().date()).days
            return max(dias_restantes, 0)
        return None
    
    def __str__(self):
        return self.descricao_resumida or "Contrato sem descrição"

    class Meta:
        verbose_name = 'Linha Orçamentária'
        verbose_name_plural = 'Linhas Orçamentárias'

# ============================================================================================================

class Remanejamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    linha_origem = models.ForeignKey(LinhaOrcamentaria, related_name='remanejamentos_origem', on_delete=models.CASCADE)
    linha_destino = models.ForeignKey(LinhaOrcamentaria, related_name='remanejamentos_destino', on_delete=models.CASCADE)
    data_remanejamento = models.DateTimeField(default=timezone.now)
    motivo = models.TextField()

    def __str__(self):
        return f"Remanejamento de {self.valor} de {self.linha_origem} para {self.linha_destino} em {self.data_remanejamento}"
    
    class Meta:
        verbose_name = 'Remanejamento'
        verbose_name_plural = 'Remanejamentos'
    
    def save(self, *args, **kwargs):
        if not self.pk:  
            self.linha_origem.valor_orcado -= self.valor
            self.linha_origem.save()
            
            self.linha_destino.valor_orcado += self.valor
            self.linha_destino.save()
        super().save(*args, **kwargs)
        
# ============================================================================================================

class Contrato(models.Model):
    linha_orcamentaria = models.OneToOneField('LinhaOrcamentaria', on_delete=models.PROTECT, related_name='contrato')
    numero_protocolo = models.CharField(max_length=7, unique=True, blank=True)
    data_assinatura = models.DateField(null=True,blank=True)
    data_vencimento = models.DateField(null=True,blank=True)
    fical_principal = models.ForeignKey('Colaborador', on_delete=models.PROTECT, related_name='contratos_fiscal_principal', verbose_name='Fiscal Principal')
    fical_substituto = models.ForeignKey('Colaborador', on_delete=models.PROTECT, related_name='contratos_fiscal_substituto', verbose_name='Fiscal Substituto')

    def save(self, *args, **kwargs):
        if not self.numero_protocolo:
            self.numero_protocolo = self.generate_protocolo()
        super().save(*args, **kwargs)

    def generate_protocolo(self):
        year_suffix = timezone.now().year % 100  
        last_protocolo = Contrato.objects.filter(numero_protocolo__endswith=f"/{year_suffix}").order_by('id').last()
        
        if last_protocolo:
            last_sequence = int(last_protocolo.numero_protocolo.split('/')[0])
            new_sequence = f"{last_sequence + 1:04}"
        else:
            new_sequence = "0001"

        return f"{new_sequence}/{year_suffix}"

    def __str__(self):
        return self.numero_contrato
    
# ============================================================================================================

class Aditivo(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='aditivos')
    data = models.DateField(null=True,blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    justificativa = models.CharField(max_length=150)

    def __str__(self):
        return f'Aditivo {self.id} - Contrato {self.contrato.numero_contrato}'