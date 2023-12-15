from django.contrib import admin
from .models import OTPModel


class OTPModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = (
        'email',
        'otp',
        'created_at',
        'updated_at',
    )
    list_display_links = (
        'email',
        'otp',
    )
    search_fields = (
        'email',
    )
    list_per_page = 25


admin.site.register(OTPModel, OTPModelAdmin)
