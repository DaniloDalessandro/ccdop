# Generated by Django 5.0.7 on 2024-07-25 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auxilios', '0005_alter_auxiliocolaborador_orcamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='auxiliocolaborador',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
