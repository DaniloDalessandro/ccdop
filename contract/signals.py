from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Orcamento, OrcamentoExterno

@receiver(post_save, sender=OrcamentoExterno)
def atualizar_orcamento_apos_save(sender, instance, **kwargs):
    orcamento = instance.ano  # instance.ano se refere ao objeto Orcamento associado
    if instance.is_deduction:
        orcamento.valor -= instance.valor
        orcamento.valor_subtraido += instance.valor
    else:
        orcamento.valor += instance.valor
        orcamento.valor_adicionado += instance.valor
    orcamento.save()

@receiver(post_delete, sender=OrcamentoExterno)
def atualizar_orcamento_apos_delete(sender, instance, **kwargs):
    orcamento = instance.ano  # instance.ano se refere ao objeto Orcamento associado
    if instance.is_deduction:
        orcamento.valor += instance.valor
        orcamento.valor_subtraido -= instance.valor
    else:
        orcamento.valor -= instance.valor
        orcamento.valor_adicionado -= instance.valor
    orcamento.save()
