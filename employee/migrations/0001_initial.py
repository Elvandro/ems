# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-16 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.PositiveIntegerField(blank=True)),
                ('department', models.CharField(choices=[('Finance', 'Finance'), ('HR', 'HR'), ('Marketing', 'Marketing'), ('Operations', 'Operations'), ('R&D', 'R&D')], max_length=30)),
                ('employee_id', models.CharField(max_length=100)),
            ],
        ),
    ]
