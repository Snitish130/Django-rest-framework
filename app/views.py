
from django.http import JsonResponse , HttpResponse
from django.http.response import Http404
from rest_framework import serializers
from app.models import Employee 
from app.serializers import EmployeeSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework import status

# function bassed view start

@csrf_exempt
def employeeListView(request):
    if request.method=='GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees , many = True)
        return JsonResponse(serializer.data , safe=False)

    elif request.method=='POST':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , safe=False)
        else:
            return JsonResponse(serializer.errors , safe=False)

@csrf_exempt
def employeeDetailView(request , pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status = 404)

    if request.method=='GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)
        
    if request.method=='DELETE':
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        
    if request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee , data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , safe=False)
        return JsonResponse(serializer.errors , safe=False)
        
def UserListView(request):
    user = User.objects.all()
    serializer = UserSerializer(user , many = True)
    return JsonResponse(serializer.data , safe=False)

# function bassed view end