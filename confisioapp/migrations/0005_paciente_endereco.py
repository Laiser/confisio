# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('confisioapp', '0004_auto_20170927_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
