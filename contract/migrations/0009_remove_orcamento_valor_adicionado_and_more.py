# Generated by Django 5.0.7 on 2024-07-19 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0008_alter_linhaorcamentaria_classe_auxilio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamento',
            name='valor_adicionado',
        ),
        migrations.RemoveField(
            model_name='orcamento',
            name='valor_subtraido',
        ),
    ]
