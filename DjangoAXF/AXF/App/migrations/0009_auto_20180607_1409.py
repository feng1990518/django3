# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_order_ordergoods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_price',
            field=models.FloatField(default=0),
        ),
    ]
