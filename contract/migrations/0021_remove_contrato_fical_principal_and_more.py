# Generated by Django 5.0.7 on 2024-08-11 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0020_contrato_mes_inicial_contrato_quantidade_prestacoes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='fical_principal',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='fical_substituto',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='mes_inicial',
        ),
        migrations.RemoveField(
            model_name='contrato',
            name='quantidade_prestacoes',
        ),
        migrations.RemoveField(
            model_name='prestacao',
            name='mes_prestacao',
        ),
        migrations.RemoveField(
            model_name='prestacao',
            name='numero_prestacao',
        ),
        migrations.RemoveField(
            model_name='prestacao',
            name='valor_pago',
        ),
        migrations.RemoveField(
            model_name='prestacao',
            name='valor_prestacao',
        ),
        migrations.AddField(
            model_name='contrato',
            name='fiscal_principal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_principal', to='contract.colaborador', verbose_name='Fiscal Principal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contrato',
            name='fiscal_substituto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_substituto', to='contract.colaborador', verbose_name='Fiscal Substituto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contrato',
            name='num_prestacoes',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestacao',
            name='data_vencimento',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestacao',
            name='numero',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prestacao',
            name='status_pagamento',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prestacao',
            name='valor_parcela',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contrato',
            name='linha_orcamentaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos', to='contract.linhaorcamentaria'),
        ),
        migrations.AlterField(
            model_name='prestacao',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.contrato'),
        ),
    ]
