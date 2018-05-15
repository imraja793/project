# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_expense', '0007_auto_20180515_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexpense',
            name='expense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_expense.Expenses'),
        ),
        migrations.AlterField(
            model_name='addexpense',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_expense.Payments'),
        ),
    ]