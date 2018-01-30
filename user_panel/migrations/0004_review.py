# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-28 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0003_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_panel.Customer')),
            ],
        ),
    ]
