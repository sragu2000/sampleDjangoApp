from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from nets.models import Departments, Employee
from nets.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
def home(request):
    return render(request, "home.html")

def contactUs(request):
    return render(request, "contactUs.html")

@csrf_exempt
def departmentApi(request, id=0):
    if request.method == "GET":
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == "POST":
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Sucessfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID = department_data["DepartmentID"])
        departments_serializer = DepartmentSerializer(department, data = department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Sucessfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == "DELETE":
        try:
            department =  Departments.objects.get(DepartmentID = id)
            # department =  Departments.objects.get(DepartmentID = 1)
            department.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except:
            return JsonResponse("Department not found", status=404, safe=False)