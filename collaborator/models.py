from django.db import models

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    mat = models.IntegerField(null=True, blank=True,verbose_name='Matrícula')
    cargo = models.CharField(max_length=50)
    fone = models.CharField(max_length=11,null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.nome_completo
    
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'