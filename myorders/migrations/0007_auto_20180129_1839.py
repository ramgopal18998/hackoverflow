# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-29 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myorders', '0006_order_bill_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(blank=True, to='cart.Cart'),
        ),
    ]
