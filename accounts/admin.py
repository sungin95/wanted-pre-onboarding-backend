from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "username",
        "email",
    )
    list_display_links = (
        "email",
        "username",
    )
    list_filter = (
        "email",
        "username",
    )
    search_fields = (
        "email",
        "username",
    )

    fieldsets = (
        (
            "info",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                    "fullname",
                    "created_at",
                    "updated_at",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_admin",
                    "is_active",
                )
            },
        ),
    )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return (
                "username",
                "email",
                "created_at",
                "updated_at",
            )
        else:
            return (
                "created_at",
                "updated_at",
            )


admin.site.register(User, UserAdmin)
