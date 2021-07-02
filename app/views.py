
import rest_framework
from app.models import Employee 
from django.http import JsonResponse
from app.serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method=='GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees , many = True)
        return Response(serializer.data)

    elif request.method=='POST':
        
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        else:
            return Response(serializer.errors )

@api_view(['GET', 'DELETE','PUT'])
def employeeDetailView(request , pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status = 404)

    if request.method=='GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
        
    if request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    if request.method=='PUT':
        
        serializer = EmployeeSerializer(employee , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors )
@api_view(['GET'])       
def UserListView(request):
    if request.method =='GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data )

# function bassed view end