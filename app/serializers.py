from app.models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
    def create(self , validated_data):
        print('create method called')
        return Employee.objects.create(**validated_data)
    def update(self , employee , validated_data):
        NewEmployee = Employee(**validated_data)
        NewEmployee.id = employee.id
        NewEmployee.save()
        print('update method called')
        return NewEmployee     
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'