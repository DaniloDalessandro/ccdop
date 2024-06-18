from django.contrib import admin
from django.db.models import Sum
from decimal import Decimal
from .models import CentroDeCustoGestor,CentroDeCustoSolicitante,Colaborador, Contrato, Orcamento, Aditivo,OrcamentoExterno,LinhaOrcamentaria,Remanejamento,Direcao,Gerencia,Coordenacao

# -------------------------------------------------------------------------------------------------------------------

@admin.register(CentroDeCustoGestor)
class CentroDeCustoGestorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

# -------------------------------------------------------------------------------------------------------------------

@admin.register(CentroDeCustoSolicitante)
class CentroDeCustoSolicitanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'centro_gestor', 'nome')
    search_fields = ('nome', 'centro_gestor__nome')
    list_filter = ('centro_gestor',)

# -------------------------------------------------------------------------------------------------------------------

class DirecaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class GerenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'direcao')
    search_fields = ('nome', 'direcao__nome')
    list_filter = ('direcao',)

class CoordenacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'gerencia')
    search_fields = ('nome', 'gerencia__nome')
    list_filter = ('gerencia',)

admin.site.register(Direcao, DirecaoAdmin)
admin.site.register(Gerencia, GerenciaAdmin)
admin.site.register(Coordenacao, CoordenacaoAdmin)

# -------------------------------------------------------------------------------------------------------------------
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'mat', 'ramal', 'email', 'direcao', 'gerencia', 'coordenacao')
    search_fields = ('nome_completo', 'mat', 'email', 'direcao__nome', 'gerencia__nome', 'coordenacao__nome')
    list_filter = ('direcao', 'gerencia', 'coordenacao')

admin.site.register(Colaborador, ColaboradorAdmin)

# -------------------------------------------------------------------------------------------------------------------

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ano', 'valor', 'valor_adicionado', 'valor_subtraido', 'centro', 'classe', 'valor_total')
    search_fields = ('ano', 'centro__nome', 'classe')
    list_filter = ('ano', 'centro', 'classe')

    def valor_total(self, obj):
        return obj.valor_total
    valor_total.short_description = 'Valor Total'

# -------------------------------------------------------------------------------------------------------------------

@admin.register(OrcamentoExterno)
class OrcamentoExternoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ano', 'valor', 'centro', 'classe', 'is_deduction')
    search_fields = ('ano__ano', 'centro', 'classe')
    list_filter = ('ano', 'classe', 'is_deduction')

# -------------------------------------------------------------------------------------------------------------------

@admin.register(LinhaOrcamentaria)
class LinhaOrcamentariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'classe', 'custo_despesa', 'centro_custo_gestor', 'centro_custo_solicitante', 'descricao_resumida', 'classificacao_orcamento', 'possivel_fiscal', 'ano_orcamento', 'tipo_contrato', 'tipo_provavel_contratacao', 'valor_orcado', 'status_elaboracao_tr', 'necessidade_contratacao', 'status_processo', 'status_contratacao')
    search_fields = ('descricao_resumida', 'centro_custo_gestor__nome', 'centro_custo_solicitante__nome')
    list_filter = ('classe', 'custo_despesa', 'classificacao_orcamento', 'tipo_contrato', 'tipo_provavel_contratacao', 'status_elaboracao_tr', 'status_processo', 'status_contratacao')

# -------------------------------------------------------------------------------------------------------------------

@admin.register(Remanejamento)
class RemanejamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor', 'linha_origem', 'linha_destino', 'data_remanejamento', 'motivo')
    search_fields = ('linha_origem__descricao_resumida', 'linha_destino__descricao_resumida', 'motivo')
    list_filter = ('data_remanejamento',)

# -------------------------------------------------------------------------------------------------------------------

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'linha_orcamentaria', 'numero_protocolo', 'data_assinatura', 'data_vencimento')
    search_fields = ('numero_protocolo', 'linha_orcamentaria__descricao_resumida')
    list_filter = ('data_assinatura', 'data_vencimento')

    def linha_orcamentaria_descricao(self, obj):
        return obj.linha_orcamentaria.descricao_resumida
    linha_orcamentaria_descricao.short_description = 'Descrição da Linha Orçamentária'

    def fiscal_principal_nome(self, obj):
        return obj.fiscal_principal.nome_completo
    fiscal_principal_nome.short_description = 'Fiscal Principal'

    def fiscal_substituto_nome(self, obj):
        return obj.fiscal_substituto.nome_completo
    fiscal_substituto_nome.short_description = 'Fiscal Substituto'

# -------------------------------------------------------------------------------------------------------------------

@admin.register(Aditivo)
class AditivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'contrato', 'data', 'valor', 'justificativa')
    search_fields = ('contrato__numero_protocolo', 'justificativa')
    list_filter = ('data',)

# -------------------------------------------------------------------------------------------------------------------

admin.site.site_header = 'Administração do Sistema'
admin.site.site_title = 'Administração do Sistema'
