from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from app.models import Students
from .serializers import studentSerializer, employeeSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee
from django.http import Http404

# Create your views here.
# def student_view(request):
#     students = Students.objects.all()
#     # print("*****************************", students)
#     students_list = list(students.values())   ------ manual serialization
#     return JsonResponse(students_list, safe=False)


@api_view(['GET', 'POST'])
def student_view(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = studentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer= studentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = studentSerializer(student,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

"""
## Class Based Views 

class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = employeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = employeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

## Class Based Views 
        
class Employee_detail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
            
            
    def get(self, request,pk):
        employee = self.get_object(pk)
        serializer = employeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        employee = self.get_object(pk)
        serializer = employeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""

""""
# Mixins

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

# Mixins 

class Employee_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request,pk)
    
    def delete(self, request, pk):
        return self.destroy(request,pk)

"""

"""
# Generics
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer

# Generics 
class Employee_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer

"""

"""
#ViewSet

class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset= Employee.objects.all()
        serializer= employeeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, pk=None):
        serializer = employeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None):
        employee= get_object_or_404(Employee, pk=pk)
        serializer = employeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = employeeSerializer(employee)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer