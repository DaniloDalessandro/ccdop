# Generated by Django 5.0.7 on 2024-07-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auxilios', '0007_alter_auxiliocolaborador_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliocolaborador',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]