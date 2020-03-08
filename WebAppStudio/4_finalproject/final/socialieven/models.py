# **************************************************************************************
# models.py
#
# Web App Studio
# Final project
#
# Robin Laponder
# 11892439
#
# **************************************************************************************

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from users.models import CustomUser

# Creates the activities.
class Activiteit(models.Model):
    name = models.CharField(max_length=128, null=True)
    gebruiker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datum = models.DateField(null=True)
    starttijd = models.CharField(max_length=5, null=True)
    eindtijd = models.CharField(max_length=5, null=True)
    straat = models.CharField(max_length=64, null=True)
    huisnummer = models.IntegerField(null=True)
    postcode = models.CharField(max_length=6, null=True)
    plaats = models.CharField(max_length=64, null=True)
    gebouw = models.IntegerField(blank=True, null=True)
    verdieping = models.IntegerField(blank=True, null=True)
    categorie = models.CharField(max_length=64, null=True)
    uitgenodigd = models.BooleanField(null=True)
    beschrijving = models.CharField(max_length=2048, null=True)

    def __str__(self):
        return f"{self.id} {self.name} van {self.gebruiker} op {self.datum}"

    class Meta:
        ordering = ['datum', 'starttijd']

# Keeps track of who is registered for which activity.
class Aanmelding(models.Model):
    activiteit = models.ForeignKey(Activiteit, on_delete=models.CASCADE)
    gebruiker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.gebruiker} gaat naar {self.activiteit}"
    
    class Meta:
        ordering = ['activiteit']

# Keeps track of nuisance reports.
class Overlast(models.Model):
    activiteit = models.ForeignKey(Activiteit, on_delete=models.CASCADE)
    gebruiker = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    beschrijving = models.CharField(max_length=2048)

    def __str__(self):
        return f"Melding van {self.gebruiker} voor {self.activiteit}"

    class Meta:
        ordering = ['activiteit']