# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_expense', '0002_addexpense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexpense',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]