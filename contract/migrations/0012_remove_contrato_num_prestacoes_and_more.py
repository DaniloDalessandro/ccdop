# Generated by Django 5.0.7 on 2024-09-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0011_prestacao_data_pagamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='num_prestacoes',
        ),
        migrations.AddField(
            model_name='contrato',
            name='tipo_pagamento',
            field=models.CharField(blank=True, choices=[('A', 'DENTRO DO PRAZO'), ('B', 'CONTRATADO NO PRAZO'), ('C', 'CONTRATADO COM ATRASO'), ('D', 'PRAZO VENCIDO'), ('E', 'LINHA TOTALMENTE REMANEJADA'), ('F', 'LINHA TOTALMENTE EXECUTADA'), ('G', 'LINHA DE PAGAMENTO'), ('H', 'LINHA PARCIALMENTE REMANEJADA'), ('I', 'LINHA PARCIALMENTE EXECUTADA'), ('J', 'N/A')], max_length=100, null=True),
        ),
    ]