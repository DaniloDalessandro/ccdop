from django.contrib import admin
from django.db.models import Sum
from decimal import Decimal
from .models import Colaborador, Contrato, Orcamento, CentroDeCusto,Aditivo,OrcamentoExterno,LinhaOrcamentaria,Remanejamento

# -------------------------------------------------------------------------------------------------------------------

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'mat', 'perfil', 'gerencia', 'ramal', 'email')
    list_filter = ('perfil', 'gerencia')
    search_fields = ('nome_completo', 'mat', 'email')
    ordering = ('nome_completo',)

# -------------------------------------------------------------------------------------------------------------------

class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'centro', 'valor', 'valor_adicionado', 'valor_subtraido', 'valor_total', 'orcamento_dop_geral')
    search_fields = ('ano', 'centro')
    list_filter = ('centro', 'ano')
    readonly_fields = ('valor_adicionado', 'valor_subtraido', 'valor_total', 'orcamento_dop_geral')

admin.site.register(Orcamento, OrcamentoAdmin)

# -------------------------------------------------------------------------------------------------------------------

class OrcamentoExternoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'centro', 'valor', 'is_deduction')
    search_fields = ('ano__ano', 'centro')
    list_filter = ('centro', 'is_deduction')

admin.site.register(OrcamentoExterno, OrcamentoExternoAdmin)

# -------------------------------------------------------------------------------------------------------------------

class CentroDeCustoAdmin(admin.ModelAdmin):
    list_display = ('diretoria', 'gerencia')
    search_fields = ('diretoria', 'gerencia')

admin.site.register(CentroDeCusto, CentroDeCustoAdmin)

# -------------------------------------------------------------------------------------------------------------------

class LinhaOrcamentariaAdmin(admin.ModelAdmin):
    list_display = (
        'descricao_resumida', 
        'classe', 
        'custo_despesa', 
        'centro_custo', 
        'tipo_contrato', 
        'valor_orcado', 
        'get_valor_utilizado', 
        'percentual_utilizacao', 
        'saldo_orcamentario_pos_remanejamento', 
        'tempo_para_contratacao'
    )
    readonly_fields = ('tempo_para_contratacao', )

    def get_valor_utilizado(self, obj):
        return obj.valor_utilizado
    get_valor_utilizado.short_description = 'Valor Utilizado'

    def tempo_para_contratacao(self, obj):
        return obj.tempo_para_contratacao
    tempo_para_contratacao.short_description = 'Tempo para Contratação'

admin.site.register(LinhaOrcamentaria, LinhaOrcamentariaAdmin)

# -------------------------------------------------------------------------------------------------------------------

class RemanejamentoAdmin(admin.ModelAdmin):
    list_display = ('valor', 'linha_origem', 'linha_destino', 'data_remanejamento')
    search_fields = ('linha_origem__nome', 'linha_destino__nome', 'motivo')
    list_filter = ('data_remanejamento',)
    date_hierarchy = 'data_remanejamento'

admin.site.register(Remanejamento, RemanejamentoAdmin)

# -------------------------------------------------------------------------------------------------------------------

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('numero_contrato', 'linha_orcamentaria', 'data_assinatura', 'data_vencimento')
    search_fields = ('numero_contrato', 'linha_orcamentaria__nome')

# -------------------------------------------------------------------------------------------------------------------

@admin.register(Aditivo)
class AditivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contrato', 'data', 'valor')
    search_fields = ('contrato__numero_contrato',)

admin.site.site_header = 'Administração do Sistema'
admin.site.site_title = 'Administração do Sistema'
