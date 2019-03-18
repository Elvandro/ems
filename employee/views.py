# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Employee
from . forms import CreateEmployeeForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def welcome(request):
    '''
    view function that renders the welcome page
    '''
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def index(request):
    '''
    view function that returns a list of all employees
    '''
    employee_list = Employee.objects.all()
    paginator = Paginator(employee_list, 10) # Show ten employees per page
    page = request.GET.get('page', 1)

    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {"employees":employees})

@login_required(login_url='/accounts/login/')
def employee(request):
    '''
    View to create an instance of an employee
    '''
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()
            return redirect('index')
    else:
        form = CreateEmployeeForm()
        return render(request, 'employee.html',{"form":form})

def update_employee(request, pk):
    '''
    view function to update an instance of an employee
    '''
    employee = get_object_or_404(Employee, pk=pk)
    form = CreateEmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        employee = form.save(commit=False)
        employee.save()
        messages.success(request, 'You have successfully updated the employee')
        return render(request, 'index.html')
    else:
        form = CreateEmployeeForm()
        return render(request, 'update_employee.html',{"form":form, "employee":employee})



def delete_employee(request, pk):
    '''
    view to delete and instance of employee
    '''
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.success(request, 'You have successfully deleted the employee')
    return render(request, 'index.html')
