from django.db import models

from stores.models import Store


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    hire_date = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'employee'


class Availability(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    is_available = models.BooleanField(default=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'employee_availability'
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.first_name} - {self.date} - {'Available' if self.is_available else 'Not Available'}"
