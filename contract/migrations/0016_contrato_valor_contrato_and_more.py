# Generated by Django 5.0.7 on 2024-07-31 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0015_delete_auxilio'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='valor_contrato',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='linhaorcamentaria',
            name='custo_despesa',
            field=models.CharField(choices=[('A', 'Base Principal'), ('B', 'Serviços Especializados'), ('C', 'Despesas Compartilhadas')], max_length=100, verbose_name='CUSTO/DESPESA'),
        ),
    ]
