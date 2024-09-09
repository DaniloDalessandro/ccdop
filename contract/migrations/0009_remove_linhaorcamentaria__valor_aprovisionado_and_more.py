# Generated by Django 5.0.7 on 2024-09-04 18:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0008_alter_orcamento_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linhaorcamentaria',
            name='_valor_aprovisionado',
        ),
        migrations.AlterField(
            model_name='contrato',
            name='valor_contrato',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='linhaorcamentaria',
            name='valor_orcado',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='orcamentoexterno',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='prestacao',
            name='valor_parcela',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='remanejamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]