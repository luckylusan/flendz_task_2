from django.shortcuts import render
from .forms import *
from employee.models import *
# Create your views here.

def home(request):
    msg = None
    success = False

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            obj = employee()
            obj.emp_id = form.cleaned_data.get("emp_id")
            obj.emp_name = form.cleaned_data.get("emp_name")
            obj.emp_designation = form.cleaned_data.get("emp_designation")
            obj.emp_doj = form.cleaned_data.get("emp_doj")


            obj.save()

            msg = 'Company created'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = EmployeeForm()

    return render(request, "index.html", {"form": form, "msg": msg, "success": success})

def employees(request):
    return render(request,"employees.html",{"data":employee.objects.all()})

def login(request):
    return render(request,'login.html')

def create_employee(request):
    return None

def register(request):
    return render(request,'reg_login/registration.html')


from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from employee.models import *
from employee.serializers import *
from rest_framework.decorators import api_view

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    try:
        tutorial = employee.objects.get(pk=pk)
    except employee.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        employee_serializer = EmployeeSerializer(tutorial)
        return JsonResponse(employee_serializer.data)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(tutorial, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data)
        return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST', 'DELETE'])
def employee_list(request):
    if request.method == 'GET':
        employe = employee.objects.all()

        title = request.query_params.get('title', None)
        if title is not None:
            employe = employe.filter(title__icontains=title)

        employee_serializer = EmployeeSerializer(employe, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = employee.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
