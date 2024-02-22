from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,
    UserProfile,
)


class UserProfileInline(admin.StackedInline):
    model = UserProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "email",
        "is_staff",
    )
    fieldsets = (
        (
            "Base Info",
            {
                "classes": ("grp-collapse",),
                "fields": (
                    "email",
                    "username",
                    "password",
                    "is_active",
                    "date_joined",
                    "last_login",
                    "user_type",
                ),
            },
        ),
        (
            "Permissions",
            {
                "classes": ("grp-collapse grp-closed",),
                "fields": (("is_staff", "is_superuser"), "user_permissions", "groups"),
            },
        ),
    )
    ordering = ("-id",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff"),
            },
        ),
    )
    # list_filter = (
    #     "is_staff",
    #     "is_superuser",
    #     "groups",
    # )
    # search_fields = ("email",)
    # readonly_fields = ("date_joined", "last_login")
    #
    # inlines = [
    #     UserProfileInline,
    # ]
