# Generated by Django 5.0.7 on 2024-09-06 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0013_remove_contrato_tipo_pagamento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestacao',
            name='numero',
        ),
    ]