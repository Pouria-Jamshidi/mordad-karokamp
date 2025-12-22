from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = [
        "id",
        "username",
        "email",
        "is_active",
        "is_superuser",
    ]

    list_display_links = ["id", "username"]
# Register your models here.
