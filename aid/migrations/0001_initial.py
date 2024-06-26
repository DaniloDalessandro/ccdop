# Generated by Django 5.0.6 on 2024-06-06 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnoAuxilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.CharField(blank=True, max_length=4, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('A', 'Graduação'), ('B', 'Pós-Graduação'), ('C', 'Auxilio creche escola')], max_length=100, null=True)),
                ('valor', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QualificacaoCooporativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demandante', models.CharField(blank=True, choices=[('A', 'GESAS'), ('B', 'GEOPE'), ('C', 'GELOG')], max_length=100, null=True)),
                ('valor_orcado', models.FloatField(blank=True, null=True)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('baneficiado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contract.colaborador')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aid.anoauxilio')),
            ],
        ),
    ]
