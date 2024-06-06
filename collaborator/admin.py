from django.contrib import admin
from .models import Colaborador

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cargo')
    search_fields = ['nome_completo', 'cargo']

admin.site.register(Colaborador, ColaboradorAdmin)