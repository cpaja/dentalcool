# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-27 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0015_auto_20171126_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odontogramapieza',
            name='cara_1_tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_cara_1', to='atencion.TratamientoDental'),
        ),
        migrations.AlterField(
            model_name='odontogramapieza',
            name='cara_2_tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_cara_2', to='atencion.TratamientoDental'),
        ),
        migrations.AlterField(
            model_name='odontogramapieza',
            name='cara_3_tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_cara_3', to='atencion.TratamientoDental'),
        ),
        migrations.AlterField(
            model_name='odontogramapieza',
            name='cara_4_tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_cara_4', to='atencion.TratamientoDental'),
        ),
        migrations.AlterField(
            model_name='odontogramapieza',
            name='cara_5_tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_cara_5', to='atencion.TratamientoDental'),
        ),
        migrations.AlterField(
            model_name='odontogramapieza',
            name='tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tratamiento_pieza', to='atencion.TratamientoDental'),
        ),
    ]