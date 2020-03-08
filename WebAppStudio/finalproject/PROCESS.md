## 05-12-2019
Vandaag heb ik geleerd:
* hoe ik Django moet upgraden naar de meest recente versie.
* hoe ik in Django een Custom User Model moet maken. Dit bleek vrij ingewikkeld en heeft me erg veel tijd gekost.
* Wat het verschil is tussen een project en een (web)app.

## 10-12-2019
Vandaag heb ik veel vooruitgang geboekt.
* Geleerd hoe je een gebruiker moet registreren met een custom User model.
```python
from django.contrib.auth import get_user_model
User = get_user_model()
```
* Liep bij het registreren van een gebruiker tegen de 'not null constraint' error aan. Dit bleek te komen doordat ik een gebruiker creëer met username, password en email en daarna pas de overige gegevens aan die gecreëerde gebruiker koppel. Op het moment dat de gebruiker wordt gecreëerd, kan python dus niet alle informatie vinden. Ik heb deze error opgelost door in models.py achter de attributes 'null=True' toe te voegen.
* Tijdens het gebruiken van de website heb ik een aantal optionele features bedacht die ik wil maken wanneer ik hier tijd voor heb:
    * In register.html het hele formulier controleren d.m.v. javascript. Op dit moment worden alleen wachtwoord en e-mail adres gecontroleerd. 
    * Een tabel maken met straten/adressen die overeenkomen met het complex Lieven en gebruikers zich alleen laten registreren wanneer de ingevoerde straat/adres in deze tabel staat.
    * In nieuwe_activiteit.html de mogelijkheid geven om het 'thuisadres' van de gebruiker te selecteren i.p.v. handmatig een adres in te voeren.
    * Een eigen logo maken. Op dit moment gebruik ik het logo van Lieven.
    * Gebruikers kunnen inloggen d.m.v. hun e-mail adres i.p.v. hun gebruikersnaam. 

## 11-12-2019
* Grootste deel van de functionaliteiten is werkend.
* Error 'NoReverseMatch. Reverse for 'nieuwe_activiteit' not found. 'nieuwe_activiteit' is not a valid view function or patternname.' opgelost:
```
href="{% url 'nieuwe_activiteit' %}"
```
moest zijn
```
href="{% url 'nieuwe activiteit' %}"
```
* Probleem wat nog niet is opgelost: Het lukt me nog niet om de 'aanmelden'-knop te verwijderen wanneer een gebruiker zich al voor die activiteit heeft aangemeld.

## 12-12-2019
* Mails verzenden met Django:
    * Maak een e-mail adres. Nadeel op dit moment is dat ik nog niet weet hoe ik mijn gegevens (mailadres en wachtwoord) kan verbergen.
    * in settings.py:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'socialieven@gmail.com'
EMAIL_HOST_PASSWORD = 'Socialieven1!'
```
    
    * in views.py:

    
```python
subject = 'Melding overlast'
message = request.POST["beschrijving"]
email_from = settings.EMAIL_HOST_USER
recipient_list = ['socialieven@gmail.com',]
send_mail( subject, message, email_from, recipient_list )

```
* Gebruikers kunnen zich alleen registreren wanneer ze in één van de juiste straten wonen.
    * Ik heb een Straat model gemaakt en daarin objecten gemaakt die overeenkomen met de straten van het wooncomplex.
    * Wanneer een gebruiker zich probeert te registeren, controleert Python of de door hen ingevoerde straat overeenkomt met een straat-object in de database.
