from django.urls import path
from .views import create_schedule, get_schedule

urlpatterns = [
    path('check/', create_schedule, name='create-schedule'),
    path('get_all_schedule/', get_schedule, name='get-weekly-schedule'),
]
