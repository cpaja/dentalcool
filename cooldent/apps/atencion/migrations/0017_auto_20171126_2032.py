# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-27 02:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0016_auto_20171126_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odontogramapieza',
            name='cara_0_tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pieza_usente', to='atencion.TratamientoDental'),
        ),
    ]
