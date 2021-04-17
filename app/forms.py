from django import forms
from employee.models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class EmployeeForm(forms.ModelForm):

    emp_id = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Employee Id",
                "class": "form-control"
            }
        ))
    emp_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Employee Name",
                "class": "form-control"
            }
        ))
    emp_designation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Employee Designation",
                "class": "form-control"
            }
        ))
    emp_doj = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={
                "placeholder": "Employee Designation",
                "class": "form-control"
            }
        ))



    class Meta:
        model = employee
        fields = ('emp_id','emp_name','emp_designation','emp_doj')