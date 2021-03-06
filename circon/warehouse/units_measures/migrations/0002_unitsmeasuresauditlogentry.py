# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-20 12:51
from __future__ import unicode_literals

import audit_log.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('units_measures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitsMeasuresAuditLogEntry',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('units_measures', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], editable=False, max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_unitsmeasures_audit_log_entry', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_permissions': (),
                'ordering': ('-action_date',),
            },
        ),
    ]
