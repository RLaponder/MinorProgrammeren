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
from .models import *

# Register your models here.
admin.site.register(Activiteit)
admin.site.register(Aanmelding)
admin.site.register(Overlast)