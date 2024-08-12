# Generated by Django 5.0.7 on 2024-08-11 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuxilioColaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('A', 'Graduação'), ('B', 'Pós-Graduação'), ('C', 'Auxilio creche escola'), ('D', 'Língua estrangeira')], max_length=100, null=True)),
                ('beneficio', models.CharField(max_length=100)),
                ('valor_parcela', models.FloatField(blank=True, null=True)),
                ('valor_total', models.FloatField(blank=True, editable=False, null=True)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('mes_inicio', models.DateField()),
                ('qtd_parcelas', models.PositiveIntegerField()),
                ('mes_fim', models.DateField(editable=False)),
                ('status', models.CharField(choices=[('aguardando', 'Aguardando'), ('ativo', 'Ativo'), ('finalizado', 'Finalizado')], default='aguardando', max_length=10)),
                ('baneficiado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contract.colaborador')),
                ('orcamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='auxilios_colaboradores', to='contract.orcamento')),
            ],
            options={
                'verbose_name': 'Auxílio Colaborador',
                'verbose_name_plural': 'Auxílios Colaboradores',
            },
        ),
    ]
