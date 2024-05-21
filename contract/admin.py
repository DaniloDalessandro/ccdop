from django.contrib import admin
from .models import Fiscal, Contrato, Orcamento, CentroDeCusto

class FiscalAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cargo')
    search_fields = ['nome_completo', 'cargo']

admin.site.register(Fiscal, FiscalAdmin)
# ------------------------------------------------
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('classe',)
    search_fields = ['classe']

admin.site.register(Contrato, ContratoAdmin)
# ------------------------------------------------
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'valor')
    search_fields = ['ano']

admin.site.register(Orcamento, OrcamentoAdmin)
# ------------------------------------------------
class CentroDeCustoAdmin(admin.ModelAdmin):
    list_display = ('centro_gestor', 'centro_solicitante')
    search_fields = ['centro_gestor', 'centro_solicitante']

admin.site.register(CentroDeCusto, CentroDeCustoAdmin)