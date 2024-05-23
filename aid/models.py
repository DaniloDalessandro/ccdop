from django.db import models
from contract.models import Colaborador

# Create your models here.

class QualificacaoCooporativa(models.Model):
    baneficiado = models.ForeignKey(Colaborador,on_delete=models.PROTECT)
    tipo_choices =  [
        ('A', 'Graduação'),
        ('B', 'Formação técnica'),
        ('C', 'Especialização'),
        ('D', 'Mestrado'),
        ('E', 'MBA'),
        ('F', 'Doutorado'),
        ('G','Auxilio creche escola'),          
    ]
    tipo = models.CharField(max_length=100,choices=tipo_choices,null=True,blank=True)
    demandante_choices =  [
        ('A', 'GESAS'),
        ('B', 'GEOPE'),
        ('C','GELOG'),          
    ]
    demandante = models.CharField(max_length=100,choices=demandante_choices,null=True,blank=True)
    valor_orcado = models.FloatField(null=True,blank=True)
    obs = models.CharField(max_length=200,null=True,blank=True)