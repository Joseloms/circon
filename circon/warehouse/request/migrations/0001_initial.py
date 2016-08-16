# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-06 21:12
from __future__ import unicode_literals

import audit_log.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_productsauditlogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_request', models.DateField(blank=True, null=True)),
                ('n_request', models.AutoField(primary_key=True, serialize=False)),
                ('applicant', models.CharField(blank=True, max_length=100)),
                ('observation', models.TextField(blank=True, max_length=250)),
                ('status', models.CharField(blank=True, default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RequestAuditLogEntry',
            fields=[
                ('date_create', models.DateField(auto_now_add=True)),
                ('date_request', models.DateField(blank=True, null=True)),
                ('n_request', models.IntegerField(blank=True, db_index=True)),
                ('applicant', models.CharField(blank=True, max_length=100)),
                ('observation', models.TextField(blank=True, max_length=250)),
                ('status', models.CharField(blank=True, default='0', max_length=1)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], editable=False, max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_request_audit_log_entry', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='RequestDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('quan_request', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Request')),
            ],
        ),
        migrations.CreateModel(
            name='RequestDetailAuditLogEntry',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('quan_request', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('action_id', models.AutoField(primary_key=True, serialize=False)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')], editable=False, max_length=1)),
                ('action_user', audit_log.models.fields.LastUserField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_requestdetail_audit_log_entry', to=settings.AUTH_USER_MODEL)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Request')),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
    ]