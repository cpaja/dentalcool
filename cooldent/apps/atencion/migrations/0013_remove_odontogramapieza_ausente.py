# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-27 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0012_auto_20171126_2002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='odontogramapieza',
            name='ausente',
        ),
    ]
