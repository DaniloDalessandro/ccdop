# Generated by Django 5.0.7 on 2024-08-11 23:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CentroDeCustoGestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100, null=True)),
                ('mat', models.IntegerField(blank=True, null=True, verbose_name='Matrícula')),
                ('ramal', models.CharField(blank=True, max_length=4, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='Coordenacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Coordenação',
                'verbose_name_plural': 'Coordenações',
            },
        ),
        migrations.CreateModel(
            name='Direcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Direção',
                'verbose_name_plural': 'Direções',
            },
        ),
        migrations.CreateModel(
            name='CentroDeCustoSolicitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('centro_gestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitantes', to='contract.centrodecustogestor')),
            ],
            options={
                'unique_together': {('centro_gestor', 'nome')},
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_protocolo', models.CharField(blank=True, editable=False, max_length=7, unique=True, verbose_name='Contrato')),
                ('data_assinatura', models.DateField(blank=True, null=True)),
                ('data_vencimento', models.DateField(blank=True, null=True)),
                ('valor_contrato', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fical_principal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_principal', to='contract.colaborador', verbose_name='Fiscal Principal')),
                ('fical_substituto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_substituto', to='contract.colaborador', verbose_name='Fiscal Substituto')),
            ],
        ),
        migrations.CreateModel(
            name='Aditivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('justificativa', models.CharField(max_length=150)),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aditivos', to='contract.contrato')),
            ],
        ),
        migrations.AddField(
            model_name='colaborador',
            name='coordenacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contract.coordenacao'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='direcao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contract.direcao'),
        ),
        migrations.CreateModel(
            name='Gerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('direcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerencias', to='contract.direcao')),
            ],
            options={
                'verbose_name': 'Gerência',
                'verbose_name_plural': 'Gerências',
                'unique_together': {('direcao', 'nome')},
            },
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='gerencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coordenacoes', to='contract.gerencia'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='gerencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contract.gerencia'),
        ),
        migrations.CreateModel(
            name='LinhaOrcamentaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe', models.CharField(blank=True, choices=[('A', 'OPEX'), ('B', 'CAPEX')], max_length=100, null=True, verbose_name='Tipo de linha')),
                ('custo_despesa', models.CharField(choices=[('A', 'Base Principal'), ('B', 'Serviços Especializados'), ('C', 'Despesas Compartilhadas')], max_length=100, verbose_name='CUSTO/DESPESA')),
                ('descricao_resumida', models.CharField(blank=True, max_length=255, null=True, verbose_name='Finalidade')),
                ('objeto', models.CharField(blank=True, max_length=255, null=True, verbose_name='Objeto')),
                ('classificacao_orcamento', models.CharField(blank=True, choices=[('NOVO', 'NOVO'), ('RENOVAÇÃO', 'RENOVAÇÃO'), ('CARY OVER', 'CARY OVER'), ('REPLANEJAMENTO', 'REPLANEJAMENTO'), ('N/A', 'N/A')], max_length=100, null=True)),
                ('tipo_contrato', models.CharField(blank=True, choices=[('I', 'SERVIÇO'), ('II', 'FORNECIMENTO'), ('III', 'ASSINATURA'), ('IV', 'FORNECIMENTO/SERVIÇO')], max_length=100, null=True)),
                ('status_linha_orcamentaria', models.CharField(blank=True, choices=[('I', 'SERVIÇO'), ('II', 'FORNECIMENTO'), ('III', 'ASSINATURA'), ('IV', 'FORNECIMENTO/SERVIÇO')], max_length=100, null=True)),
                ('_valor_aprovisionado', models.FloatField(default=0.0)),
                ('tipo_provavel_contratacao', models.CharField(choices=[('A', 'LICITAÇÃO'), ('B', 'DISPENSA EM RAZÃO DO VALOR'), ('C', 'CONVÊNIO'), ('D', 'FUNDO FIXO'), ('E', 'INEXIGIBILIDADE'), ('F', 'ATA DE REGISTRO DE PREÇO'), ('H', 'ACORDO DE COOPERAÇÃO'), ('I', 'APOSTILAMENTO')], max_length=100)),
                ('valor_orcado', models.FloatField(blank=True, default=0, null=True)),
                ('status_elaboracao_tr', models.CharField(blank=True, choices=[('I', 'VENCIDO'), ('II', 'DENTRO DO PRAZO'), ('III', 'ELABORADO COM ATRASO'), ('IV', 'ELABORADO NO PRAZO')], max_length=100, null=True)),
                ('necessidade_contratacao', models.DateField(blank=True, null=True)),
                ('status_processo', models.CharField(blank=True, choices=[('I', 'PLANEJAMENTO'), ('II', 'Execução'), ('III', 'Elaboração de TR'), ('IV', 'Cotação'), ('V', 'Em proc. aditivo')], max_length=100, null=True)),
                ('status_contratacao', models.CharField(blank=True, choices=[('A', 'DENTRO DO PRAZO'), ('B', 'CONTRATADO NO PRAZO'), ('C', 'CONTRATADO COM ATRASO'), ('D', 'PRAZO VENCIDO'), ('E', 'LINHA TOTALMENTE REMANEJADA'), ('F', 'LINHA TOTALMENTE EXECUTADA'), ('G', 'LINHA DE PAGAMENTO'), ('H', 'LINHA PARCIALMENTE REMANEJADA'), ('I', 'LINHA PARCIALMENTE EXECUTADA'), ('J', 'N/A')], max_length=100, null=True)),
                ('obs_contrato', models.TextField(blank=True, max_length=400, null=True)),
                ('centro_custo_gestor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contract.centrodecustogestor')),
                ('centro_custo_solicitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contract.centrodecustosolicitante')),
                ('possivel_fiscal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscal_possivel', to='contract.colaborador', verbose_name='Fiscal')),
            ],
            options={
                'verbose_name': 'Linha Orçamentária',
                'verbose_name_plural': 'Linhas Orçamentárias',
            },
        ),
        migrations.AddField(
            model_name='contrato',
            name='linha_orcamentaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contrato', to='contract.linhaorcamentaria'),
        ),
        migrations.CreateModel(
            name='Orcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('classe', models.CharField(blank=True, choices=[('A', 'OPEX'), ('B', 'CAPEX')], max_length=100, null=True)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('centro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.centrodecustogestor')),
            ],
            options={
                'verbose_name': 'Orçamento',
                'verbose_name_plural': 'Orçamentos',
                'unique_together': {('ano', 'centro', 'classe')},
            },
        ),
        migrations.AddField(
            model_name='linhaorcamentaria',
            name='ano_orcamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contratos', to='contract.orcamento'),
        ),
        migrations.CreateModel(
            name='OrcamentoExterno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('centro', models.CharField(max_length=20)),
                ('classe', models.CharField(blank=True, choices=[('OPEX', 'OPEX'), ('CAPEX', 'CAPEX')], max_length=100, null=True)),
                ('tipo_movimentacao', models.CharField(choices=[('entrada', 'Entrada'), ('retirada', 'Retirada')], max_length=8)),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orcamentos_externos', to='contract.orcamento')),
            ],
            options={
                'verbose_name': 'Orçamento Externo',
                'verbose_name_plural': 'Orçamentos Externos',
            },
        ),
        migrations.CreateModel(
            name='Remanejamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_remanejamento', models.DateTimeField(default=django.utils.timezone.now)),
                ('motivo', models.TextField()),
                ('linha_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remanejamentos_destino', to='contract.linhaorcamentaria')),
                ('linha_origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remanejamentos_origem', to='contract.linhaorcamentaria')),
            ],
            options={
                'verbose_name': 'Remanejamento',
                'verbose_name_plural': 'Remanejamentos',
            },
        ),
        migrations.AlterUniqueTogether(
            name='coordenacao',
            unique_together={('gerencia', 'nome')},
        ),
    ]
