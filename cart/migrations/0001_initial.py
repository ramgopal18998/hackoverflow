# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-26 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_panel', '0002_auto_20180125_1819'),
        ('products', '0005_productdata_dicount_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=50, null=True)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=50, null=True)),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_panel.Customer')),
            ],
        ),
    ]
