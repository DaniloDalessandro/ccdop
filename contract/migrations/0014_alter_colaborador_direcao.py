# Generated by Django 5.0.7 on 2024-07-29 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0013_alter_colaborador_coordenacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='direcao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contract.direcao'),
        ),
    ]
