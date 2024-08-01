# Generated by Django 5.0.7 on 2024-07-29 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auxilios', '0011_alter_auxiliocolaborador_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='auxiliocolaborador',
            name='beneficio',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auxiliocolaborador',
            name='tipo',
            field=models.CharField(blank=True, choices=[('A', 'Graduação'), ('B', 'Pós-Graduação'), ('C', 'Auxilio creche escola'), ('D', 'Língua estrangeira')], max_length=100, null=True),
        ),
    ]