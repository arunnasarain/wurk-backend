from django.urls import path
from .views import update_attendance,get_one_attendance

urlpatterns = [
    path('check/', get_one_attendance, name='attendance_check'),
    path('update/', update_attendance, name='update_attendance')
]
