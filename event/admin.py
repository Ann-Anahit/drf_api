from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'owner', 'event_start', 'created_at']
    search_fields = ['title', 'description', 'owner__username']
    list_filter = ['event_start', 'created_at', 'updated_at']
    ordering = ['-created_at']
