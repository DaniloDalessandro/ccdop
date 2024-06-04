from django.contrib import admin
from .models import Colaborador, Contrato, Orcamento, CentroDeCusto,Aditivo,OrcamentoExterno
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cargo')
    search_fields = ['nome_completo', 'cargo']

admin.site.register(Colaborador, ColaboradorAdmin)
# ------------------------------------------------
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('classe','aviso_fiscal')
    search_fields = ['classe']
    readonly_fields = ('aviso_fiscal','elaboracao_tr','abertura_tr')

    def aviso_fiscal(self, obj):
        return obj.aviso_fiscal
    aviso_fiscal.short_description = 'Aviso ao Fiscal'

    def elaboracao_tr(self, obj):
        return obj.elaboracao_tr
    elaboracao_tr.short_description = 'Elaboração de TR'

    def abertura_tr(self, obj):
        return obj.abertura_tr
    abertura_tr.short_description = 'Abertura de TR no ECM'

admin.site.register(Contrato, ContratoAdmin)
# ------------------------------------------------
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'valor', 'valor_adicionado', 'valor_subtraido', 'valor_total')

    def valor_adicionado(self, obj):
        return obj.valor_adicionado
    valor_adicionado.short_description = 'Valor Adicionado'

    def valor_subtraido(self, obj):
        return obj.valor_subtraido
    valor_subtraido.short_description = 'Valor Subtraído'

    def valor_total(self, obj):
        return obj.valor_total
    valor_total.short_description = 'Valor Total'

admin.site.register(Orcamento, OrcamentoAdmin)
# ------------------------------------------------
class CentroDeCustoAdmin(admin.ModelAdmin):
    list_display = ('centro_gestor', 'centro_solicitante')
    search_fields = ['centro_gestor', 'centro_solicitante']

admin.site.register(CentroDeCusto, CentroDeCustoAdmin)
# ------------------------------------------------
class AditivoAdmin(admin.ModelAdmin):
    list_display = ('data_aditivo', 'descricao')
    search_fields = ['data_aditivo', 'descricao']

admin.site.register(Aditivo, AditivoAdmin)
# ------------------------------------------------
class OrcamentoExternoAdmin(admin.ModelAdmin):
    list_display = ('diretoria',)
    search_fields = ['diretoria']

admin.site.register(OrcamentoExterno,OrcamentoExternoAdmin)

