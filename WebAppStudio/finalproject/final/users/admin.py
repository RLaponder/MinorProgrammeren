# **************************************************************************************
# admin.py
#
# Web App Studio
# Final project
#
# Robin Laponder
# 11892439
#
# **************************************************************************************

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import *

# Add CustomUser attributes to admin page.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('geboortedatum', 'straat', 'huisnummer', 'postcode', 'woonplaats', 'gebouw', 'verdieping')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Straat)