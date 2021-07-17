from .models import User
from django.contrib import admin


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    fields = (
        'email', 'phone', 'password', 'first_name', 'last_name',
        'is_verified', 'is_staff', 'is_superuser', 'is_active',
        'last_login')