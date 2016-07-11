# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160705_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'permissions': (('to_access_warehouse', 'Puede acceder a almacen'), ('add_entry', 'Puede agregar a entrada'), ('update_entry', 'Puede actualizar a entrada'), ('delete_entry', 'Puede eliminar a entrada'), ('add_exit', 'Puede agregar a salida'), ('update_exit', 'Puede actualizar a salida'), ('delete_exit', 'Puede eliminar a salida'), ('to_access_inventory', 'Puede acceder a inventario'), ('to_access_request', 'Puede acceder a solicitudes'), ('to_access_search', 'Puede acceder a busquedas'))},
        ),
    ]
