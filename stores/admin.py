from django.contrib import admin

from .models import Store, Group


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'city', 'state', 'country', 'zipcode')
    search_fields = ('name', 'city', 'state', 'country')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

