from rest_framework import serializers
from .models import Employee, Availability


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'position', 'store', 'other_fields']  # Adjust fields as needed

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['id', 'employee', 'date', 'is_available', 'start_time', 'end_time']