from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'store', 'date', 'shift_type', 'start_time', 'end_time', 'employee']

class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['store', 'date', 'shift_type', 'start_time', 'end_time', 'employee']
