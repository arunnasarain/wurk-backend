from django.contrib import admin

from schedule.models import Schedule


# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('store', 'date', 'shift_type', 'start_time', 'end_time')
    search_fields = ('store__name', 'date', 'shift_type')
    list_filter = ('store', 'shift_type', 'date')
    ordering = ('date', 'shift_type')
