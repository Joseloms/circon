# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_auto_20160706_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='id',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='n_purchase',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]