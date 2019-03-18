# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.
class Employee(models.Model):
    DEPARTMENT_CHOICES = (
    ('Finance', 'Finance'),
    ('HR', 'HR'),
    ('Marketing', 'Marketing'),
    ('Operations', 'Operations'),
    ('R&D','R&D')
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=50,blank=True)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    employee_id = models.CharField(max_length=100,unique=True,default=uuid.uuid4)

    def __str__(self):
        return self.first_name

    def save_employee(self):
        self.save()

    def delete_employee(self):
        self.delete()
