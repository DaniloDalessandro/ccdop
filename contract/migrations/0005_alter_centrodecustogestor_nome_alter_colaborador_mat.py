# Generated by Django 5.0.7 on 2024-08-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0004_alter_coordenacao_nome_alter_direcao_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centrodecustogestor',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='mat',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Matrícula'),
        ),
    ]
