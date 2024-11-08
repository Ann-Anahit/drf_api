from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp', 'text')
    search_fields = ('sender__username', 'recipient__username', 'text')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')

# Register the models with the custom admin classes
admin.site.register(Message, MessageAdmin)

