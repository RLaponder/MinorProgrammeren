# **************************************************************************************
# urls.py
#
# Web App Studio
# Final project
#
# Robin Laponder
# 11892439
#
# **************************************************************************************

from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('profiel', views.profiel, name='profiel')
]
      