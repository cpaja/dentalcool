# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-17 00:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atencion', '0005_auto_20171116_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='odontograma',
            old_name='informes',
            new_name='informe',
        ),
    ]
