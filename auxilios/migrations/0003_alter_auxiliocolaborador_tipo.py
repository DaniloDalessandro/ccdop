# Generated by Django 5.0.7 on 2024-09-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auxilios', '0002_alter_auxiliocolaborador_valor_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliocolaborador',
            name='tipo',
            field=models.CharField(blank=True, choices=[('Graduação', 'Graduação'), ('Pós-Graduação', 'Pós-Graduação'), ('Auxilio creche escola', 'Auxilio creche escola'), ('Língua estrangeira', 'Língua estrangeira')], max_length=100, null=True),
        ),
    ]
