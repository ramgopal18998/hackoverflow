# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-28 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.CharField(max_length=50)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=50, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ManyToManyField(to='cart.Cart')),
            ],
        ),
    ]