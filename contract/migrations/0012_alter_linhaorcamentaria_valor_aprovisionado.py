# Generated by Django 5.0.7 on 2024-07-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0011_linhaorcamentaria_status_linha_orcamentaria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linhaorcamentaria',
            name='valor_aprovisionado',
            field=models.FloatField(default=0.0),
        ),
    ]
