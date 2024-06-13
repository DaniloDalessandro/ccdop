# Generated by Django 5.0.6 on 2024-06-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0006_remove_contrato_numero_contrato_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orcamento',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='classe',
            field=models.CharField(blank=True, choices=[('A', 'OPEX'), ('B', 'CAPEX')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orcamentoexterno',
            name='classe',
            field=models.CharField(blank=True, choices=[('A', 'OPEX'), ('B', 'CAPEX')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='centro',
            field=models.CharField(choices=[('DOP', 'DOP'), ('GELOG', 'GELOG'), ('GEOPE', 'GEOPE'), ('GESAS', 'GESAS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='orcamentoexterno',
            name='centro',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orcamentoexterno',
            name='is_deduction',
            field=models.BooleanField(default=False, verbose_name='Envio de Orçamento'),
        ),
        migrations.AlterUniqueTogether(
            name='orcamento',
            unique_together={('ano', 'centro', 'classe')},
        ),
    ]
