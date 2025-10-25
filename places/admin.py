from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'types', 'address', 'created_by']
    list_filter = ['types', 'created_at']
    search_fields = ['name', 'address']