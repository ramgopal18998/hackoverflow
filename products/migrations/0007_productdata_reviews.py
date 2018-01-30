# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-28 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0004_review'),
        ('products', '0006_auto_20180128_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='reviews',
            field=models.ForeignKey(default=21, on_delete=django.db.models.deletion.CASCADE, to='user_panel.Review'),
            preserve_default=False,
        ),
    ]
