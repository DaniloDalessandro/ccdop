from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import OrcamentoExterno, Orcamento

@receiver(post_save, sender=OrcamentoExterno)
def update_orcamento_total_on_save(sender, instance, **kwargs):
    orcamento = instance.ano
    orcamento.valor_total += instance.valor or 0
    orcamento.save()

@receiver(pre_delete, sender=OrcamentoExterno)
def update_orcamento_total_on_delete(sender, instance, **kwargs):
    orcamento = instance.ano
    orcamento.valor_total -= instance.valor or 0
    orcamento.save()
