from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from contract.models import Direcao,Gerencia,Coordenacao

class CustomUserManager(BaseUserManager):
    def create_user(self, email, cpf, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        if not cpf:
            raise ValueError('O CPF deve ser fornecido')

        email = self.normalize_email(email)
        user = self.model(email=email, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O superusuário deve ter is_superuser=True.')

        return self.create_user(email, cpf, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    PRESIDENCIA = 'presidencia'
    DIRETOR = 'diretor'
    GERENTE = 'gerente'
    COORDENADOR = 'coordenador'
    ANALISTA = 'analista'

    PERFIL_CHOICES = [
        (PRESIDENCIA, 'Presidência'),
        (DIRETOR, 'Diretor'),
        (GERENTE, 'Gerente'),
        (COORDENADOR, 'Coordenador'),
        (ANALISTA, 'Analista'),
    ]
    perfil = models.CharField(max_length=30, choices=PERFIL_CHOICES)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=255,verbose_name='Nome Completo')
    direcao = models.ForeignKey(Direcao, null=True, blank=True, on_delete=models.SET_NULL)
    gerencia = models.ForeignKey(Gerencia, null=True, blank=True, on_delete=models.SET_NULL)
    coordenacao = models.ForeignKey(Coordenacao, null=True, blank=True, on_delete=models.SET_NULL)
    telefone = models.CharField(max_length=15,verbose_name='Ramal')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  
        blank=True,
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cpf']

    def __str__(self):
        return self.email
