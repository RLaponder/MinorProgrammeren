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
    path('', views.index, name='index'),
    path('activiteiten', views.activiteiten, name='activiteiten'),
    path('nieuwe_activiteit', views.nieuwe_activiteit, name='nieuwe activiteit'),
    path('aanmelden/<int:id>', views.aanmelden, name='aanmelden'),
    path('afmelden/<int:id>', views.afmelden, name='afmelden'),
    path('overlast/<int:id>', views.overlast, name='overlast'),
    path('mijn_activiteiten', views.mijn_activiteiten, name='mijn activiteiten'),
    path('mijn_aanmeldingen', views.mijn_aanmeldingen, name='mijn aanmeldingen')
]