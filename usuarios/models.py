from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from contract.models import Direcao,Gerencia,Coordenacao
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=100, null=True)
    mat = models.IntegerField(null=True, blank=True, verbose_name='Matrícula')
    direcao = models.ForeignKey('contract.Direcao', on_delete=models.CASCADE, null=True, blank=True)
    gerencia = models.ForeignKey('contract.Gerencia', on_delete=models.SET_NULL, null=True, blank=True)
    coordenacao = models.ForeignKey('contract.Coordenacao', on_delete=models.SET_NULL, null=True, blank=True)
    ramal = models.CharField(max_length=4, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)






