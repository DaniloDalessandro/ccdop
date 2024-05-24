from django.db import models
from contract.models import Colaborador

# Create your models here.
class AnoAuxilio(models.Model):
    ano = models.CharField(max_length=4,null=True,blank=True)
    tipo_choices = [
        ('A', 'Graduação'),
        ('B', 'Pós-Graduação'),
        ('C','Auxilio creche escola'),          
    ]
    tipo = models.CharField(max_length=100,choices=tipo_choices,null=True,blank=True)
    valor = models.FloatField(default=0)

    def __str__(self):
        tipo_dict = dict(self.tipo_choices)
        tipo_descricao = tipo_dict.get(self.tipo, 'Tipo desconhecido')
        return f"{self.ano} - {tipo_descricao}"
    


class QualificacaoCooporativa(models.Model):
    baneficiado = models.ForeignKey(Colaborador,on_delete=models.PROTECT)
    tipo = models.ForeignKey(AnoAuxilio,on_delete=models.PROTECT)
    demandante_choices =  [
        ('A', 'GESAS'),
        ('B', 'GEOPE'),
        ('C','GELOG'),          
    ]
    demandante = models.CharField(max_length=100,choices=demandante_choices,null=True,blank=True)
    valor_orcado = models.FloatField(null=True,blank=True)
    obs = models.CharField(max_length=200,null=True,blank=True)