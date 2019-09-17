from django.contrib import admin

from .models import UserProfile


class UserAdminFields(admin.ModelAdmin):
    list_display = ("user",  "first_name", "last_name", "profile_image", "joined")


admin.site.register(UserProfile, UserAdminFields)