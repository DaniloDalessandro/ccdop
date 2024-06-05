from django.contrib import admin
from .models import Colaborador, Contrato, Orcamento, CentroDeCusto,Aditivo

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cargo')
    search_fields = ['nome_completo', 'cargo']

admin.site.register(Colaborador, ColaboradorAdmin)
# ------------------------------------------------
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('classe',)
    search_fields = ['classe']

admin.site.register(Contrato, ContratoAdmin)
# ------------------------------------------------
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'valor', 'centro', 'orcamento_dop_geral')
    readonly_fields = ('orcamento_dop_geral',)

    def orcamento_dop_geral(self, obj):
        return obj.orcamento_dop_geral

    orcamento_dop_geral.short_description = 'Orçamento DOP Geral'

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