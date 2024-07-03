from django.urls import path
from .views import get_one_employee, create_or_update_availability, get_availability, get_employee_availability

urlpatterns = [
    path('get_one_employee/', get_one_employee, name='get_one_employee'),

    path('availability/', create_or_update_availability, name='create_or_update_availability'),
    path('availability/<int:employee_id>/', get_availability, name='get_availability'),
    path('employee_availability/<int:employee_id>/', get_employee_availability, name='get_employee_availability'),
]
