from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance, Employee
from .serializers import AttendanceSerializer


@api_view(['GET'])
def get_one_attendance(request):
    try:
        attendance = Attendance.objects.first()
        if not attendance:
            return JsonResponse({'error': 'No attendance records found.'}, status=404)

        serializer = AttendanceSerializer(attendance)
        return JsonResponse(serializer.data, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['PUT'])
def update_attendance(request):
    data = request.data
    employee_id = data.get('employee_id')
    date = data.get('date')  # Date format: 'YYYY-MM-DD'
    status = data.get('status')
    check_in_time = data.get('check_in_time')  # Time format: 'HH:MM:SS'
    check_out_time = data.get('check_out_time')  # Time format: 'HH:MM:SS'

    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        attendance, created = Attendance.objects.get_or_create(
            employee=employee,
            date=date,
            defaults={'status': status, 'check_in_time': check_in_time, 'check_out_time': check_out_time}
        )

        if not created:
            attendance.status = status
            attendance.check_in_time = check_in_time
            attendance.check_out_time = check_out_time
            attendance.save()

        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
# Mark an employee's attendance
# employee = Employee.objects.get(id=1)
# attendance, created = Attendance.objects.get_or_create(
#     employee=employee,
#     date='2024-07-01',
#     defaults={'status': 'P'}
# )
# # Update attendance status if already exists
# if not created:
#     attendance.status = 'A'
#     attendance.save()
