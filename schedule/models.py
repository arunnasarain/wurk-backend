from django.db import models

from employees.models import Employee
from stores.models import Store


# Create your models here.
class Schedule(models.Model):
    SHIFT_CHOICES = [
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening'),
        ('N', 'Night'),
    ]

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    shift_type = models.CharField(max_length=1, choices=SHIFT_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('store', 'date', 'shift_type')
        ordering = ['date', 'shift_type']
        db_table = 'schedule'

    def __str__(self):
        return f"{self.store.name} - {self.date} - {self.get_shift_type_display()}"

class Break(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='breaks')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.schedule} - {self.start_time} to {self.end_time}"

    class Meta:
        db_table = 'break'