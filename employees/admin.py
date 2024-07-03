from django.contrib import admin

from .models import Employee, Availability


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'hire_date', 'store')
    search_fields = ('first_name', 'last_name', 'email', 'store__name')
    list_filter = ('store', 'hire_date')


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'is_available', 'start_time', 'end_time')
    search_fields = ('employee__name', 'date')
    list_filter = ('is_available', 'date', 'employee__store')

    def get_queryset(self, request):
        # Custom queryset to show only availability records related to the current user's store
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(employee__store__in=request.user.stores.all())


admin.site.register(Availability, AvailabilityAdmin)
