# Generated by Django 5.0.6 on 2024-05-23 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnoAuxilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('A', 'Graduação'), ('B', 'Pós-Graduação'), ('C', 'Auxilio creche escola')], max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='qualificacaocooporativa',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='aid.anoauxilio'),
        ),
    ]
