from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee, Availability
from .serializers import EmployeeSerializer, AvailabilitySerializer


@api_view(['GET'])
def get_one_employee(request):
    try:
        employee = Employee.objects.first()
        if not employee:
            return JsonResponse({'error': 'No employee records found.'}, status=404)

        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['POST'])
def create_or_update_availability(request):
    data = request.data
    employee_id = data.get('employee')
    date = data.get('date')
    is_available = data.get('is_available')
    start_time = data.get('start_time')
    end_time = data.get('end_time')

    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found.'}, status=status.HTTP_404_NOT_FOUND)

    availability, created = Availability.objects.update_or_create(
        employee=employee,
        date=date,
        defaults={'is_available': is_available, 'start_time': start_time, 'end_time': end_time}
    )

    serializer = AvailabilitySerializer(availability)
    return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


@api_view(['GET'])
def get_availability(request, employee_id):
    date = request.GET.get('date')

    if not date:
        return Response({'error': 'date parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        availability = Availability.objects.get(employee_id=employee_id, date=date)
    except Availability.DoesNotExist:
        return Response({'error': 'Availability record not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AvailabilitySerializer(availability)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_employee_availability(request, employee_id):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if not start_date or not end_date:
        return Response({'error': 'start_date and end_date parameters are required.'},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

    availabilities = Availability.objects.filter(employee_id=employee_id, date__range=[start_date, end_date])
    serializer = AvailabilitySerializer(availabilities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)