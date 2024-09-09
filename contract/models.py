from django.db import models
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal
from django.utils import timezone
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from django.core.validators import MinValueValidator


# ============================================================================================================

class CentroDeCustoGestor(models.Model):
    nome = models.CharField(max_length=100,unique=True)

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

class Direcao(models.Model):
    nome = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Direção'
        verbose_name_plural = 'Direções'
        

class Gerencia(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    direcao = models.ForeignKey(Direcao, on_delete=models.CASCADE, related_name='gerencias')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Gerência'
        verbose_name_plural = 'Gerências'
        unique_together = ('direcao','nome')

class Coordenacao(models.Model):
    nome = models.CharField(max_length=100,unique=True)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE, related_name='coordenacoes')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Coordenação'
        verbose_name_plural = 'Coordenações'
        unique_together = ('gerencia','nome')

# ============================================================================================================

class Colaborador(models.Model):
    
    nome_completo = models.CharField(max_length=100, null=True)
    mat = models.IntegerField(null=True, blank=True,verbose_name='Matrícula',unique=True)     
    direcao = models.ForeignKey(Direcao, on_delete=models.CASCADE,null=True)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.SET_NULL,null=True)
    coordenacao = models.ForeignKey(Coordenacao, on_delete=models.SET_NULL,null=True)
    ramal = models.CharField(max_length=4,null=True, blank=True)
    email = models.EmailField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.nome_completo or "Colaborador sem Nome"
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

# ============================================================================================================

class Orcamento(models.Model):
    ano = models.IntegerField()
    centro = models.ForeignKey(CentroDeCustoGestor, on_delete=models.CASCADE)
    CLASSE_CHOICES = [
        ('A', 'OPEX'),
        ('B', 'CAPEX'),
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0,validators=[MinValueValidator(0.01)] )

    @property
    def valores_adicionados(self):
        if self.pk:
            return self.orcamentos_externos.filter(tipo_movimentacao='entrada').aggregate(total=Sum('valor'))['total'] or 0
        return 0

    @property
    def valores_enviados(self):
        if self.pk:
            return self.orcamentos_externos.filter(tipo_movimentacao='retirada').aggregate(total=Sum('valor'))['total'] or 0
        return 0

    @property
    def valor_total(self):
        if self.pk:
            return self.valor + self.valores_adicionados - self.valores_enviados
        return self.valor

    @property
    def orcamento_total(self):
        if self.pk:
            orcamentos_internos = Orcamento.objects.filter(ano=self.ano, centro=self.centro).aggregate(total=Sum('valor'))['total'] or 0
            orcamentos_externos = OrcamentoExterno.objects.filter(ano=self).aggregate(total=Sum('valor'))['total'] or 0
            return orcamentos_internos + orcamentos_externos
        return self.valor
    
    @property
    def valor_restante(self):
        linhas_orcamentarias = self.contratos.all()  # Accessing via related_name
        total_linhas = sum(Decimal(linha.valor_orcado) for linha in linhas_orcamentarias)
        return self.valor - total_linhas

    def __str__(self):
        return f"{self.ano} - {self.centro}"

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
        unique_together = ('ano', 'centro', 'classe')

# ============================================================================================================

class OrcamentoExterno(models.Model):
    ENTRADA_RETIRADA_CHOICES = [
        ('entrada', 'Entrada'),
        ('retirada', 'Retirada'),
    ]

    ano = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='orcamentos_externos')
    valor = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.01)])
    centro = models.CharField(max_length=20)
    CLASSE_CHOICES = [
        ('OPEX', 'OPEX'),
        ('CAPEX', 'CAPEX'),
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True)
    tipo_movimentacao = models.CharField(max_length=8, choices=ENTRADA_RETIRADA_CHOICES)

    def save(self, *args, **kwargs):
        # Verifica se o orçamento principal já foi salvo
        if not self.ano.pk:
            self.ano.save()

        # Armazena valores antigos antes de salvar
        old_valor = None
        old_tipo_movimentacao = None
        if self.pk:
            old_instance = OrcamentoExterno.objects.get(pk=self.pk)
            old_valor = old_instance.valor
            old_tipo_movimentacao = old_instance.tipo_movimentacao

        super().save(*args, **kwargs)

        # Atualiza o valor do orçamento principal
        if old_valor is not None and old_tipo_movimentacao is not None:
            if old_tipo_movimentacao == 'entrada':
                self.ano.valor -= old_valor
            elif old_tipo_movimentacao == 'retirada':
                self.ano.valor += old_valor

        if self.tipo_movimentacao == 'entrada':
            self.ano.valor += self.valor
        elif self.tipo_movimentacao == 'retirada':
            self.ano.valor -= self.valor

        self.ano.save()

    def delete(self, *args, **kwargs):
        # Atualizar orçamento ao deletar
        if self.tipo_movimentacao == 'entrada':
            self.ano.valor -= self.valor
        elif self.tipo_movimentacao == 'retirada':
            self.ano.valor += self.valor
        self.ano.save()
        super().delete(*args, **kwargs)

    

    class Meta:
        verbose_name = 'Orçamento Externo'
        verbose_name_plural = 'Orçamentos Externos'

    def __str__(self):
        return f"{self.ano} - {self.centro} - {self.get_tipo_movimentacao_display()}"

# ============================================================================================================

class LinhaOrcamentaria(models.Model):
    CLASSE_CHOICES = [
        ('OPEX', 'OPEX'),
        ('CAPEX', 'CAPEX'),
    ]
    classe = models.CharField(max_length=100, choices=CLASSE_CHOICES, blank=True, null=True, verbose_name='Tipo de linha')

    CUSTODESPESA_CHOICES = [
        ('A', 'Base Principal'),
        ('B', 'Serviços Especializados'),
        ('C', 'Despesas Compartilhadas'),
        # Outros valores...
    ]
    custo_despesa = models.CharField(max_length=100, choices=CUSTODESPESA_CHOICES, verbose_name='CUSTO/DESPESA')

    centro_custo_gestor = models.ForeignKey(CentroDeCustoGestor, on_delete=models.SET_NULL, null=True, blank=True)
    centro_custo_solicitante = models.ForeignKey(CentroDeCustoSolicitante, on_delete=models.SET_NULL, null=True, blank=True)
    descricao_resumida = models.CharField(max_length=255, null=True, blank=True, verbose_name='Finalidade')
    objeto = models.CharField(max_length=80, blank=True, null=True, verbose_name='Objeto')

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

    STATUS_LINHA_ORCAMENTARIA_CHOICES = [
        ('I', 'SERVIÇO'),
        ('II', 'FORNECIMENTO'),
        ('III', 'ASSINATURA'),
        ('IV', 'FORNECIMENTO/SERVIÇO'),
    ]
    status_linha_orcamentaria = models.CharField(max_length=100, choices=STATUS_LINHA_ORCAMENTARIA_CHOICES, blank=True, null=True)

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
    tipo_provavel_contratacao = models.CharField(max_length=100, choices=TIPOCONTRATACAOPROVAVEL_CHOICES)
    valor_orcado = models.FloatField(default=0, blank=True, null=True,validators=[MinValueValidator(0.01)])

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

    def saldo_disponivel(self):
        total_contratos = self.contratos.aggregate(total=Sum('valor_contrato'))['total'] or Decimal('0.0')
        saldo = Decimal(self.valor_orcado) - total_contratos
        return saldo
    
    def update_valor_aprovisionado(self):
        self._valor_aprovisionado = self.contratos.aggregate(total=Sum('valor_contrato'))['total'] or 0.0
        self.save(update_fields=['_valor_aprovisionado'])

    def save(self, *args, **kwargs):
        if self.ano_orcamento and self.valor_orcado > self.ano_orcamento.valor_restante:
            raise ValidationError('O valor orçado excede o valor restante do orçamento.')
        super().save(*args, **kwargs)

    @property
    def valor_aprovisionado(self):
        return self._valor_aprovisionado

    @property
    def valor_utilizado(self):
        return self.valor_aprovisionado

    @property
    def valor_remanejado_total(self):
        remanejamentos_origem = self.remanejamentos_origem.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        remanejamentos_destino = self.remanejamentos_destino.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        return remanejamentos_origem + remanejamentos_destino

    @property
    def saldo_orcamentario_pos_remanejamento(self):
        valor_remanejado_origem = self.remanejamentos_origem.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        valor_remanejado_destino = self.remanejamentos_destino.aggregate(total=Sum('valor'))['total'] or Decimal(0.0)
        saldo = Decimal(self.valor_orcado) + valor_remanejado_destino - valor_remanejado_origem - Decimal(self.valor_utilizado)
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
    valor = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.01)])
    linha_origem = models.ForeignKey(LinhaOrcamentaria, related_name='remanejamentos_origem', on_delete=models.CASCADE)
    linha_destino = models.ForeignKey(LinhaOrcamentaria, related_name='remanejamentos_destino', on_delete=models.CASCADE)
    data_remanejamento = models.DateTimeField(default=timezone.now)
    motivo = models.TextField()

    def clean(self):
        saldo_disponivel = Decimal(self.linha_origem.valor_orcado) - Decimal(self.linha_origem.valor_aprovisionado)
        if self.valor > saldo_disponivel:
            raise ValidationError(f"O valor do remanejamento ({self.valor}) não pode exceder o saldo disponível ({saldo_disponivel}).")

    def save(self, *args, **kwargs):
        # Executar validações antes de salvar
        self.clean()
        
        if not self.pk:  # Novo remanejamento
            self.linha_origem.valor_orcado -= self.valor
            self.linha_origem.save()
            
            self.linha_destino.valor_orcado += self.valor
            self.linha_destino.save()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Remanejamento de {self.valor} de {self.linha_origem} para {self.linha_destino} em {self.data_remanejamento}"
    
    class Meta:
        verbose_name = 'Remanejamento'
        verbose_name_plural = 'Remanejamentos'

        
# ============================================================================================================

class Contrato(models.Model):
    linha_orcamentaria = models.ForeignKey(LinhaOrcamentaria, on_delete=models.PROTECT, related_name='contratos')
    numero_protocolo = models.CharField(max_length=7, unique=True, blank=True, editable=False, verbose_name='Contrato')
    data_assinatura = models.DateField(null=True, blank=True)
    data_vencimento = models.DateField(null=True, blank=True)
    fiscal_principal = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='contratos_fiscal_principal', verbose_name='Fiscal Principal')
    fiscal_substituto = models.ForeignKey(Colaborador, on_delete=models.PROTECT, related_name='contratos_fiscal_substituto', verbose_name='Fiscal Substituto')
    valor_contrato = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.01)])
    TIPO_PAGAMENTO_CHOICES = [
        ('PAGAMENTO ÚNICO','PAGAMENTO ÚNICO'),
        ('PAGAMENTO ANUAL','PAGAMENTO ANUAL'),
        ('PAGAMENTO SEMANAL','PAGAMENTO SEMANAL'),
        ('PAGAMENTO MENSAL','PAGAMENTO MENSAL'),
        ('PAGAMENTO QUIZENAL','PAGAMENTO QUINZENAL'),
        ('PAGAMENTO TRIMESTRAL','PAGAMENTO TRIMESTRAL'),
        ('PAGAMENTO SEMESTRAL','PAGAMENTO SEMESTRAL'),
        ('PAGAMENTO SOB DEMANDA','PAGAMENTO SOB DEMANDA'),
    ]
    natureza_pagamento = models.CharField(choices=TIPO_PAGAMENTO_CHOICES,max_length=30)
    
    def save(self, *args, **kwargs):
        saldo_disponivel = self.linha_orcamentaria.saldo_disponivel()

        if self.valor_contrato > saldo_disponivel:
            raise ValueError(f"O valor do contrato ({self.valor_contrato}) excede o saldo disponível ({saldo_disponivel}) na linha orçamentária.")

        if not self.numero_protocolo:
            self.numero_protocolo = self.generate_protocolo()
        

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.linha_orcamentaria.update_valor_aprovisionado()

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
        return self.descricao or "Linha Orçamentária sem Descrição"


from django.db import models
from django.core.validators import MinValueValidator

from django.db import models
from django.core.validators import MinValueValidator

class Prestacao(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE)
    numero_parcela = models.PositiveIntegerField(editable=False)  # O número da parcela será gerado automaticamente
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    data_pagamento = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Se for uma nova prestação (sem ID)
            # Verifica quantas prestações já existem para este contrato
            total_prestacoes = Prestacao.objects.filter(contrato=self.contrato).count()
            # Define o próximo número da parcela
            self.numero_parcela = total_prestacoes + 1

        super(Prestacao, self).save(*args, **kwargs)

    def __str__(self):
        return f'Prestação {self.numero_parcela} do contrato {self.contrato.numero_protocolo}'


    
# ============================================================================================================

class Aditivo(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='aditivos')
    data = models.DateField(null=True,blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True,default=0.0)
    justificativa = models.CharField(max_length=150)

    def __str__(self):
        return f'Aditivo {self.id} - Contrato {self.contrato.numero_protocolo}'
    
# ============================================================================================================

