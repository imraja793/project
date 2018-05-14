# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_title', models.CharField(max_length=20, verbose_name='Expense Title')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('currency', models.CharField(max_length=23, verbose_name='Currency')),
                ('vendor_name', models.CharField(blank=True, max_length=200, verbose_name='Vendor Name')),
                ('last4digit', models.IntegerField()),
                ('invoice', models.IntegerField()),
                ('userid', models.IntegerField()),
            ],
        ),
    ]