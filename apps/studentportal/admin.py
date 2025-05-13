from django.contrib import admin
from .models import Studentprtal, Notification


admin.site.register(Studentprtal)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'receiver', 'send_to_all', 'created_at']
    list_filter = ['send_to_all', 'created_at']
    search_fields = ['title', 'body', 'receiver__first_name', 'receiver__last_name']