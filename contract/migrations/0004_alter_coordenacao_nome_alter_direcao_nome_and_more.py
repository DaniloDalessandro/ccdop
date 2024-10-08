# Generated by Django 5.0.7 on 2024-08-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0003_alter_contrato_num_prestacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordenacao',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='direcao',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='gerencia',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
