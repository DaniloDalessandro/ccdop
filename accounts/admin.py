from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'cpf', 'nome','telefone')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'cpf', 'nome', 'telefone','perfil','direcao','gerencia','coordenacao', 'is_active', 'is_staff', 'groups', 'user_permissions')

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'cpf', 'nome','perfil','direcao','gerencia','coordenacao', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('cpf', 'nome','telefone')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'cpf', 'nome', 'telefone','perfil','direcao','gerencia','coordenacao', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'cpf', 'nome')
    ordering = ('nome',)

admin.site.register(CustomUser, CustomUserAdmin)

