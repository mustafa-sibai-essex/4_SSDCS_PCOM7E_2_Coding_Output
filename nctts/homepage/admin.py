from django.contrib import admin
from homepage.models import Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInline(admin.StackedInline):
    """Assigns the account class to the admin user registration page"""
    model = Account
    can_delete = False
    verbose_name_plural = "Accounts"


class CustomizeUserAdmin(UserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User, CustomizeUserAdmin)
