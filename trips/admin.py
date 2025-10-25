from django.contrib import admin
from .models import Destination, Trip, TripDay, DayDestination

class DayDestinationInline(admin.TabularInline):
    model = DayDestination
    extra = 1
    fields = ['destination', 'order', 'start_time', 'end_time', 'notes']

class TripDayInline(admin.TabularInline):
    model = TripDay
    extra = 1
    fields = ['day_number', 'date']

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'country', 'category', 'created_by']
    list_filter = ['category', 'city', 'country']
    search_fields = ['name', 'city', 'country']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'start_date', 'end_date', 'privacy', 'created_at']
    list_filter = ['privacy', 'created_at', 'start_date']
    search_fields = ['title', 'description', 'owner__username']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [TripDayInline]

@admin.register(TripDay)
class TripDayAdmin(admin.ModelAdmin):
    list_display = ['trip', 'day_number', 'date']
    list_filter = ['trip', 'date']
    inlines = [DayDestinationInline]

@admin.register(DayDestination)
class DayDestinationAdmin(admin.ModelAdmin):
    list_display = ['trip_day', 'destination', 'order', 'start_time', 'end_time']
    list_filter = ['trip_day__trip']
    ordering = ['trip_day', 'order']