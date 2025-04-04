# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import RegistrationForm  # This should now match

class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm
    # Add any additional customizations here if needed
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')

# Unregister the default User admin and register our custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)