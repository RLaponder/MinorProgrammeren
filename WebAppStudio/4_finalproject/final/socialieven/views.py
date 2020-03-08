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
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    # If user tries to login, do the following.
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                "loggedin": True
            }
            return redirect(index)
        else:
            context = {
                "loggedin": False,
                "message": "Het ingevoerde e-mail adres of wachtwoord is onjuist."
            }
            return render(request, "users/index.html", context)
    
    # Check whether a user is logged in, and go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
    else:
        context = {
            "user": request.user,
            "loggedin": True
        }
    return render(request, "users/index.html", context)


def activiteiten(request):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    
    # Get all the activities from database and show them.
    context = {
        "activiteiten": Activiteit.objects.all(),
        "aanmeldingen": Aanmelding.objects.filter(gebruiker=request.user),
        "loggedin": True
    }
    return render(request, "users/activiteiten.html", context)


def nieuwe_activiteit(request):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)

    # If the user submits the activity form, do the following.
    if request.method == "POST": 
        # Create a new activity for this user.
        activiteit = Activiteit(gebruiker=request.user)
        
        # Add all the entered information from the form to the created activity.
        activiteit.name = request.POST["naam"]
        activiteit.datum = request.POST["datum"]
        activiteit.starttijd = request.POST["starttijd"]
        activiteit.eindtijd = request.POST["eindtijd"]
        activiteit.straat = request.POST["straat"]
        if request.POST["huisnummer"] != '':
            activiteit.huisnummer = int(request.POST["huisnummer"])
        activiteit.postcode = request.POST["postcode"]
        activiteit.plaats = request.POST["plaats"]
        if request.POST["gebouw"] != '':
            activiteit.gebouw = int(request.POST["gebouw"])
        if request.POST["verdieping"] != '':
            activiteit.verdieping = int(request.POST["verdieping"])
        activiteit.categorie = request.POST["categorie"]
        if request.POST["uitgenodigd"] == "Ja":
            activiteit.uitgenodigd = True
        else:
            activiteit.uitgenodigd = False
        activiteit.beschrijving = request.POST["beschrijving"]
        activiteit.save()

        # Add the user to their own activity.
        aanmelding = Aanmelding(activiteit=activiteit, gebruiker=request.user)
        aanmelding.save()

        context = {
            "message": "Succes! Je activiteit is toegevoegd.",
            "loggedin": True
        }
        return render(request, "users/nieuwe_activiteit.html", context)
    
    # Show the form.
    context = {
        "loggedin": True
    }
    return render(request, "users/nieuwe_activiteit.html", context)


def aanmelden(request, id):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    
    # Get the activity that the user wants to register to.
    activiteit = Activiteit.objects.get(id=id)

    # Get all the registrations for the user.
    aanmeldingen = Aanmelding.objects.filter(gebruiker=request.user)
    
    # Check whether the user already registered for this activity. If yes, show message.
    for aanmelding in aanmeldingen:
        if activiteit == aanmelding.activiteit :
            context = {
                "loggedin": True,
                "message": "Oeps! Je hebt je al aangemeld voor deze activiteit..."
            }
            return render(request, "users/activiteiten.html", context)
    
    # Register the user to the activity.
    aanmelding = Aanmelding(activiteit=activiteit, gebruiker=request.user)
    aanmelding.save()
    
    # Get context and render webpage.
    context = {
            "message": "Succes! Je bent je aangemeld.",
            "activiteiten": Activiteit.objects.all(),
            "aanmeldingen": Aanmelding.objects.filter(gebruiker=request.user),
            "loggedin": True
    }
    return render(request, "users/activiteiten.html", context)


def afmelden(request, id):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    
    # Get the activity that the user wants to unregister to.
    activiteit = Activiteit.objects.get(id=id)
    
    # Delete the registration for this activity.
    aanmelding = Aanmelding.objects.get(activiteit=activiteit, gebruiker=request.user)
    aanmelding.delete()
    
    # Get context and render webpage.
    context = {
            "message": "Succes! Je bent afgemeld.",
            "activiteiten": Activiteit.objects.all(),
            "aanmeldingen": Aanmelding.objects.filter(gebruiker=request.user),
            "loggedin": True
    }
    return render(request, "users/activiteiten.html", context)


def overlast(request, id):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    
    # If a user reports a nuisance, do the following.
    if request.method == "POST": 
        # Add report to database.
        activiteit = Activiteit.objects.get(id=id)
        beschrijving = request.POST["beschrijving"]
        melding = Overlast(activiteit=activiteit, gebruiker=request.user, beschrijving=beschrijving)
        melding.save()
        gebruiker = activiteit.gebruiker.first_name

        # Create a message and send it via email.
        subject = 'Melding overlast'
        message_header = (
        f"""Beste {gebruiker},\n\nEen medebewoner geeft aan overlast te ervaren van de door jou georganiseerde activiteit en stuurt het volgende bericht:\n\n""")
        message_body = f"{beschrijving}"
        message_footer = f"\n\nAfzender: {request.user.first_name} {request.user.last_name}"
        message = f"{message_header}{message_body}{message_footer}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [activiteit.gebruiker.email]
        send_mail(subject, message, email_from, recipient_list)

        # Get context and render webpage.
        context = {
            "loggedin": True,
            "message": "Succes! Je melding is verwerkt en de organisator zal spoedig je bericht ontvangen.",
            "activiteit": Activiteit.objects.get(id=id),
            "aanmeldingen": Aanmelding.objects.filter(gebruiker=request.user)
        }
        return render(request, "users/overlast.html", context)
    
    # Get context and render webpage.
    context = {
        "loggedin": True,
        "activiteit": Activiteit.objects.get(id=id)
    }
    return render(request, "users/overlast.html", context)

def mijn_activiteiten(request):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "message": "Helaas! Je moet ingelogd zijn om deze pagina te bezoeken.",
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    
    # Show all activities created by the current user.
    context = {
        "loggedin": True,
        "activiteiten": Activiteit.objects.filter(gebruiker=request.user)
    }
    return render(request, "users/mijn_activiteiten.html", context)


def mijn_aanmeldingen(request):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "message": "Helaas! Je moet ingelogd zijn om deze pagina te bezoeken.",
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    
    # Show all activities the current user had registerd to.
    context = {
        "loggedin": True,
        "aanmeldingen": Aanmelding.objects.filter(gebruiker=request.user)
    }
    return render(request, "users/mijn_aanmeldingen.html", context)