from rest_framework import serializers
from app.models import Students
from employee.models import Employee

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee 
        fields = "__all__"