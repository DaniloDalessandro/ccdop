# Generated by Django 5.0.7 on 2024-09-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0014_remove_prestacao_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestacao',
            name='numero_parcela',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
