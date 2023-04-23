from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext as _

from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "profile_picture", "bio")
    filter_horizontal = ("followers", "following")


admin.site.register(User, UserAdmin)
