# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-27 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0013_remove_odontogramapieza_ausente'),
    ]

    operations = [
        migrations.AddField(
            model_name='odontogramapieza',
            name='pieza_usente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pieza_usente', to='atencion.TratamientoDental'),
        ),
    ]
