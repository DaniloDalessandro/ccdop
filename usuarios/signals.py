from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario
from contract.models import Colaborador

@receiver(post_save, sender=Usuario)
def criar_colaborador(sender, instance, created, **kwargs):
    if created:
        Colaborador.objects.create(
            nome_completo=instance.nome_completo,
            mat=instance.mat,
            direcao=instance.direcao,
            gerencia=instance.gerencia,
            coordenacao=instance.coordenacao,
            ramal=instance.ramal,
            email=instance.email
        )
