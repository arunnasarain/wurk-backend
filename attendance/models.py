from django.db import models

from employees.models import Employee


# Create your models here.
class Attendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('E', 'Excused'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=ATTENDANCE_CHOICES, default='P')
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'attendance'
        unique_together = ('employee', 'date')
        ordering = ['date']

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"
