# Generated by Django 5.0.7 on 2024-09-06 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0009_remove_linhaorcamentaria__valor_aprovisionado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestacao',
            name='data_pagamento',
        ),
        migrations.RemoveField(
            model_name='prestacao',
            name='data_vencimento',
        ),
        migrations.RemoveField(
            model_name='prestacao',
            name='status_pagamento',
        ),
    ]