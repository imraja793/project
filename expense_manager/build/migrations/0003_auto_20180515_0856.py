# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 08:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0002_auto_20180515_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='mobile_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(b'^\\d{1,10}$')]),
        ),
    ]
