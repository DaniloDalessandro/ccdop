from django.db import models
from contract.models import Colaborador,CentroDeCustoGestor

class QualificacaoCooporativa(models.Model):
    baneficiado = models.ForeignKey(Colaborador,on_delete=models.PROTECT)    
    demandante = models.ForeignKey(CentroDeCustoGestor,on_delete=models.PROTECT)
    tipo_choices = [
        ('A', 'Graduação'),
        ('B', 'Pós-Graduação'),
        ('C','Auxilio creche escola'),          
    ]
    tipo = models.CharField(max_length=100,choices=tipo_choices,null=True,blank=True)
    valor_orcado = models.FloatField(null=True,blank=True)
    obs = models.CharField(max_length=200,null=True,blank=True)