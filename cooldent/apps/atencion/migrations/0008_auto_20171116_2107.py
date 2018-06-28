# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-17 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0007_examenesauxiliares'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiadetalle',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consulta',
            name='motivo',
            field=models.CharField(blank=True, choices=[('Control de tratamiento', 'Control de tratamiento'), ('Limpieza', 'Limpieza'), ('Primera Consulta', 'Primera COnsulta'), ('Urgencia', 'Urgencia')], max_length=255, null=True, verbose_name='Motivo de la consulta'),
        ),
    ]