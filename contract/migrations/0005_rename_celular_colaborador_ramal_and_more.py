# Generated by Django 5.0.6 on 2024-06-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0004_remove_linhaorcamentaria_data_prevista_tr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaborador',
            old_name='celular',
            new_name='ramal',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='cargo',
        ),
        migrations.RemoveField(
            model_name='colaborador',
            name='fone',
        ),
        migrations.AddField(
            model_name='colaborador',
            name='perfil',
            field=models.CharField(choices=[('A', 'DIREÇÃO'), ('B', 'GERENCIA'), ('C', 'COORDENAÇÃO')], default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='gerencia',
            field=models.CharField(choices=[('A', 'GELOG'), ('B', 'GEOPE'), ('C', 'GESAS')], max_length=50),
        ),
    ]
