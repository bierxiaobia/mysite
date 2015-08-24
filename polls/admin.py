from django.contrib import admin
from models import User


class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_active')

admin.site.register(User, AdminUser)