# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-17 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190316_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
