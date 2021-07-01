from app.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)
    
    def create(self , validated_data):
        print('create method called')
        return Employee.objects.create(**validated_data)
    def update(self , employee , validated_data):
        NewEmployee = Employee(**validated_data)
        NewEmployee.id = employee.id
        NewEmployee.save()
        print('update method called')
        return NewEmployee     
        
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    

