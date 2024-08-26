from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUsuarioAdmin(UserAdmin):
    # Campos a serem exibidos na página de listagem
    list_display = ('username', 'nome_completo', 'email', 'mat', 'direcao', 'gerencia', 'coordenacao', 'ramal', 'is_staff', 'is_active')
    # Campos de pesquisa
    search_fields = ('username', 'nome_completo', 'email')
    # Filtragem lateral
    list_filter = ('is_staff', 'is_active', 'direcao', 'gerencia', 'coordenacao')
    
    # Definição dos campos a serem exibidos no formulário de edição de usuários
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'email', 'mat', 'ramal')}),
        ('Informações Organizacionais', {'fields': ('direcao', 'gerencia', 'coordenacao')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Campos exibidos ao criar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'nome_completo', 'email', 'mat', 'ramal', 'direcao', 'gerencia', 'coordenacao', 'is_active', 'is_staff')}
        ),
    )
    
    # Campos somente leitura (opcional)
    readonly_fields = ('last_login', 'date_joined')

# Registrando o modelo Usuario com a customização
admin.site.register(Usuario, CustomUsuarioAdmin)

