# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confisioapp', '0003_paciente_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='pederiodo_avaliacao',
            new_name='periodo_avaliacao',
        ),
    ]
