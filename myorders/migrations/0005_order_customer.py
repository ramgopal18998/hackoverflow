# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-28 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0005_customer_type'),
        ('myorders', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_panel.Customer'),
        ),
    ]
