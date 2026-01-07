from django.contrib import admin
from .models import BookingRequest


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "service_type", "event_date", "status", "created_at")
    list_filter = ("status", "service_type", "created_at")
    search_fields = ("full_name", "email", "phone", "location", "message")
