from rest_framework import serializers
from nets.models import Departments
from nets.models import Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ("DepartmentID", "DepartmentName")

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("EmployeeID","EmployeeName","Department","DateOfJoining","PhotoFileName")