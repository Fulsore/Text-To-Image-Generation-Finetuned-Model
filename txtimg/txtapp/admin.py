# Admin Configuration
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser

class UserAdmin(BaseUserAdmin):
    list_display = ["id", "email", "username", "is_admin", "is_superuser"]
    list_filter = ["is_admin", "is_superuser"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal Info", {"fields": ["username"]}),
        ("Permissions", {"fields": ["is_admin", "is_superuser", "is_active"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email", "username"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(MyUser, UserAdmin)