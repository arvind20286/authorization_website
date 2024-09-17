from django.contrib import admin
from .models import *
# Register your models here.

class AuthProviderAdmin(admin.ModelAdmin):
  list_display = ['name']
admin.site.register(AuthProvider, AuthProviderAdmin)

class UserAdmin(admin.ModelAdmin):
  list_display = ['email', 'password', 'google_id', 'auth_provider']
admin.site.register(User, UserAdmin)