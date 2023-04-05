from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    # when display the user model in the admin panel, the following fields are shown
    list_display = ["email", "first_name", "last_name", "is_staff", "is_active"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )

    # when creating a new user, the password fields are shown
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = [
        "email",
        "first_name",
        "last_name",
    ]
    ordering = ["email", "first_name", "last_name"]
    filter_horizontal = []


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
