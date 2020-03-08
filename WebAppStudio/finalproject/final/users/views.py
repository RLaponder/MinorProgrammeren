# **************************************************************************************
# views.py
#
# Web App Studio
# Final project
#
# Robin Laponder
# 11892439
#
# **************************************************************************************

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from users.models import *
from socialieven.views import *
import datetime

# Use custom User model.
from django.contrib.auth import get_user_model
User = get_user_model()


def logout_view(request):
    # Log user out and go to index.
    logout(request)
    return redirect(index)


def register(request):
    # If a user submits the register form, do the following.
    if request.method == "POST": 
        # Check if user actually lives in one of the right streets. If not, go to index and show message.
        straat = request.POST["straat"].capitalize()
        try:
            straat = Straat.objects.get(straatnaam=straat)
        except:
            context = {
                "message": "Helaas. Om gebruik te maken van SociaLieven, moet je bewoner zijn van Lieven.",
                "loggedin": False
            }
            return render(request, "users/index.html", context)         

        # Create a new user object.
        user = User.objects.create_user(username=request.POST["gebruikersnaam"], email=request.POST["email1"], password=request.POST["wachtwoord1"])
        
        # Add all data from the form to this user.
        user.first_name = request.POST["voornaam"].capitalize()
        user.last_name = request.POST["achternaam"].capitalize()
        user.geboortedatum = request.POST["geboortedatum"]
        user.straat = request.POST["straat"].capitalize()
        user.huisnummer = int(request.POST["huisnummer"])
        user.postcode = request.POST["postcode"]
        user.woonplaats = request.POST["woonplaats"].capitalize()
        user.gebouw = int(request.POST["gebouw"])
        user.verdieping = int(request.POST["verdieping"])
        user.save()
        
        # Succesfull registration, go to index.
        context = {
            "loggedin": False,
            "message": "Succes! Je bent geregistreerd je kunt nu inloggen."
        }
        return render(request, "users/index.html", context)
    
    # Show the register form.
    return render(request, "users/register.html")


def profiel(request):
    # Go to login page if the user has not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False,
            "message": "Helaas! Je moet ingelogd zijn om deze pagina te bezoeken."
        }
        return render(request, "users/index.html", context)
    
    # Show the profile of the current user.
    context = {
        "user": request.user,
        "loggedin": True
    }
    return render(request, "users/profiel.html", context)