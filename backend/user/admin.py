from django.contrib import admin

from user.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "gender",
        "marital_status",
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "phone_number",
        "email",
    )
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
