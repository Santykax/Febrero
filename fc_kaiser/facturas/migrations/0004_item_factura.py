# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-28 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0003_auto_20180228_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturas.Factura'),
        ),
    ]
