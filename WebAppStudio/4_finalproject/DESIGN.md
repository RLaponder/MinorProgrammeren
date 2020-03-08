# Final Project - technical overview

### Index<br>
*Dit is de eerste pagina die een gebruiker te zien krijgt en fungeert als homepage.*<br>

url: /''<br>
functie: socialieven.views.index<br>
bestanden: index.html<br>
functionaliteit:<br>
* **Inloggen**<br>
<p align="center">
    <img src="doc/index_login_final.png" alt="Index pagina" width="200"/>
</p>

### Registreren<br>
*Op deze pagina ziet de gebruiker een formulier dat hij/zij moet invullen om zich te registreren.*<br>
url: /register<br>
functie: users.views.register<br>
bestanden: register.html<br>
functionaliteit:<br>
* **Registreren van een gebruiker**<br>
<p align="center">
    <img src="doc/register_functionaliteit_final.png" alt="Index pagina" width="300"/>
</p>

### Uitloggen<br>
*Wanneer een gebruiker is ingelogd, kan hij/zij via de navbar uitloggen.*<br>
url: /logout<br>
functie: users.views.logout_view<br>
bestanden: -
functionaliteit:<br>
* **Uitloggen van een gebruiker**<br>

### Activiteiten<br>
*Deze pagina geeft een overzicht van alle activiteiten die zijn gecreëerd door alle gebruikers.*<br>

url: /activiteiten<br>
functie: socialieven.views.activiteiten<br>
bestanden: activiteiten.html<br>
functionaliteit:<br>
* **Activiteiten weergeven**<br>
<p align="center">
    <img src="doc/activiteiten_functionaliteit_final.png" alt="Index pagina" width="300"/>
</p>

* **Aanmelden**<br>
*Een gebruiker kan zich voor een activiteit aanmelden, door op de 'aanmelden'-knop te klikken.*<br>
url: /aanmelden/id<br>
functie: socialieven.views.aanmelden<br>
bestanden: -<br>
* **Afmelden**<br>
*Wanneer een gebruiker is aangemeld voor een activiteit, kan hij/zich zich afmelden door op de 'afmelden'-knop te klikken.*<br>
url: /afmelden/id<br>
functie: socialieven.views.afmelden<br>
bestanden: -<br>
* **Overlast**<br>
*Een gebruiker kan op de 'overlast'-knop klikken, om overlast te melden van een activiteit. De gebruiker komt op een pagina waarop een formulier ingevuld moet worden, dat vervolgens per mail verzonden wordt aan de organisator van de betreffende activiteit.*<br>
url: /overlast/id<br>
functie: socialieven.views.overlast<br>
bestanden: overlast.html<br>
functionaliteit:<br>
* **Overlast melden**<br>
<p align="center">
    <img src="doc/overlast_functionaliteit_final.png" alt="Index pagina" width="300"/>
</p>

### Nieuwe activiteit<br>
*Door middel van een formulier, kan een gebruiker een activiteit creëren, die vervolgens wordt weergegeven op de 'activiteiten'-pagina.*

url: /nieuwe_activiteit<br>
functie: socialieven.views.nieuwe_activiteit<br>
bestanden: nieuwe_activiteit.html<br>
* **Nieuwe activiteit creëren**<br>
<p align="center">
    <img src="doc/nieuweactiviteit_functionaliteit_final.png" alt="Index pagina" width="300"/>
</p>

### Profiel<br>
*Op deze pagina ziet een gebruiker zijn/haar persoonlijke informatie.*<br>

url: /profiel<br>
functie: users.views.profiel<br>
bestanden: profiel.html<br>
functionaliteit:<br>
* **Persoonlijke informatie bekijken**<br>
<p align="center">
    <img src="doc/profiel_functionaliteit_final.png" alt="Index pagina" width="300"/>
</p>

### Mijn activiteiten<br>
*Deze pagina laat zien welke activiteiten gecreëerd zijn door de gebruiker.*<br>

url: /mijn_activiteiten<br>
functie: socialieven.views.mijn_activiteiten<br>
bestanden: mijn_activiteiten.html<br>
functionaliteit:<br>
* **Door gebruiker gemaakte activiteiten weergeven**<br>

### Mijn aanmeldingen<br>
*Hier ziet een gebruiker voor welke activiteiten hij/zij zichzelf heeft aangemeld. Voor eigen activiteiten wordt de gebruiker automatisch aangemeld en ook deze activiteiten zijn te zien op deze pagina.*<br>

url: /mijn_aanmeldingen<br>
functie: socialieven.views.mijn_aanmeldingen<br>
bestanden: mijn_aanmeldingen.html<br>
functionaliteit:<br>
* **Weergeven van activiteiten waar gebruiker voor aangemeld is**<br>