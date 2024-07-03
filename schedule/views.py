from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Store, Employee, Schedule, Break
from datetime import datetime, timedelta


@api_view(['POST'])
def create_schedule(request):
    data = request.data
    store_id = data.get('store_id')
    date = data.get('date')  # Date format: 'YYYY-MM-DD'
    employee_ids = data.get('employee_ids', [])

    try:
        store = Store.objects.get(id=store_id)
        employees = Employee.objects.filter(id__in=employee_ids, store=store)

        schedules_created = []
        for i, employee in enumerate(employees):
            start_time = datetime.strptime(data.get('start_time', '09:00'), '%H:%M').time()
            end_time = datetime.strptime(data.get('end_time', '17:00'), '%H:%M').time()
            schedule, created = Schedule.objects.get_or_create(
                employee=employee,
                date=date,
                defaults={'start_time': start_time, 'end_time': end_time}
            )

            if created:
                create_breaks(schedule, i, len(employees))

            schedules_created.append(schedule)

        return JsonResponse({'message': f'Schedules created for {len(schedules_created)} employees.'}, status=201)

    except Store.DoesNotExist:
        return JsonResponse({'error': 'Store not found.'}, status=404)

    except Employee.DoesNotExist:
        return JsonResponse({'error': 'One or more employees not found in this store.'}, status=404)


def create_breaks(schedule, employee_index, total_employees):
    shift_duration = datetime.combine(datetime.today(), schedule.end_time) - datetime.combine(datetime.today(),
                                                                                              schedule.start_time)
    shift_hours = shift_duration.total_seconds() / 3600

    if shift_hours >= 8:
        create_8_hour_breaks(schedule, employee_index, total_employees)
    elif shift_hours >= 4:
        create_4_hour_breaks(schedule)


def create_4_hour_breaks(schedule):
    start_time = datetime.combine(datetime.today(), schedule.start_time)
    midpoint = start_time + timedelta(hours=2)
    create_break(schedule, midpoint.time(), (midpoint + timedelta(minutes=15)).time())


def create_8_hour_breaks(schedule, employee_index, total_employees):
    start_time = datetime.combine(datetime.today(), schedule.start_time)
    for i in range(4):
        break_start = start_time + timedelta(hours=i * 2 + (employee_index * 15 // total_employees))
        create_break(schedule, break_start.time(), (break_start + timedelta(minutes=15)).time())
    # Additional 30-minute lunch break
    lunch_break_start = start_time + timedelta(hours=4)
    create_break(schedule, lunch_break_start.time(), (lunch_break_start + timedelta(minutes=30)).time())


def create_break(schedule, start_time, end_time):
    Break.objects.create(schedule=schedule, start_time=start_time, end_time=end_time)


@api_view(['GET'])
def get_schedule(request):
    store_id = request.GET.get('store_id')
    week_start_date = request.GET.get('week_start_date')  # Date format: 'YYYY-MM-DD'

    try:
        store = Store.objects.get(id=store_id)
        week_start_date = datetime.strptime(week_start_date, '%Y-%m-%d').date()
        week_end_date = week_start_date + timedelta(days=6)  # Assuming a 7-day week

        schedules = Schedule.objects.filter(employee__store=store,
                                            date__range=[week_start_date, week_end_date]).order_by('date')

        schedule_data = []
        for schedule in schedules:
            print("$$$", schedule.employee)

            breaks = schedule.breaks.all()
            breaks_data = [{'start_time': b.start_time, 'end_time': b.end_time} for b in breaks]
            schedule_data.append({
                'employee': f"{schedule.employee.first_name} {schedule.employee.last_name}",
                'date': schedule.date,
                'start_time': schedule.start_time,
                'end_time': schedule.end_time,
                'breaks': breaks_data
            })

        return JsonResponse({'schedules': schedule_data}, status=200)

    except Store.DoesNotExist:
        return JsonResponse({'error': 'Store not found.'}, status=404)
#
# # Assume this function is in your view or model for creating a schedule
# def create_schedule(store_id, employee_id, date, start_time, end_time):
#     store = Store.objects.get(id=store_id)
#     employee = Employee.objects.get(id=employee_id)
#
#     # Calculate shift duration
#     start_datetime = datetime.combine(date, start_time)
#     end_datetime = datetime.combine(date, end_time)
#     shift_duration = end_datetime - start_datetime
#
#     # Create breaks
#     if shift_duration >= timedelta(hours=8):
#         break_time1 = start_time + timedelta(hours=4)
#         break_time2 = start_time + timedelta(hours=6)
#         break_duration = timedelta(minutes=15)
#         lunch_break_time = start_time + timedelta(hours=4)  # 30-minute break around lunchtime
#         breaks = [(break_time1, break_time1 + break_duration), (break_time2, break_time2 + break_duration), (lunch_break_time, lunch_break_time + timedelta(minutes=30))]
#     elif shift_duration >= timedelta(hours=4):
#         break_time = start_time + timedelta(hours=2)
#         break_duration = timedelta(minutes=15)
#         breaks = [(break_time, break_time + break_duration)]
#     else:
#         breaks = []
#
#     # Create schedule entry
#     schedule = Schedule.objects.create(
#         store=store,
#         employee=employee,
#         date=date,
#         start_time=start_time,
#         end_time=end_time
#     )
#
#     # Create break times
#     for start, end in breaks:
#         Break.objects.create(
#             schedule=schedule,
#             start_time=start,
#             end_time=end
#         )
