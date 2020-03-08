# Final project - assessment

## Code
Ik heb mijn best gedaan om alle code en de database zorgvuldig te ontwerpen. Dit heb ik gedaan door middel van onder andere indentatie, duidelijke comments, witregels, en duidelijke namen voor variabelen. Daarnaast heb ik leren werken met een Custom User model. Hier heb ik voor gekozen, omdat ik graag extra informatie van een gebruiker wilde opslaan. Tijdens het werken aan de opdracht kwam ik er wel achter dat ik in totaal wat meer models nodig had dan ik van tevoren had ingeschat.

## Interactieontwerp
Ik denk dat de website gemakkelijk te gebruiken is door anderen. Wel bevat de pagina nog relatief weinig inhoud, doordat dit uiteindelijk vooral moet worden toegevoegd door gebruikers. Gebruikers moeten zich uiteindelijk registreren en activiteiten creëren waar anderen zich weer voor kunnen aanmelden. 

## Repository
Naar mijn mening is mijn repository op orde. Ik heb geprobeerd om overzichtelijk te werken door mijn project te verdelen in twee applicaties ('users' en 'socialieven'), zodat verschillende functies van elkaar gescheiden zijn. 


## Projectdocumentatie
Ik denk dat de verschillende markdown bestanden, in combinatie met meerdere screenshots, er voor zorgen dat het project duidelijk gedocumenteerd is. Ik merk dat ik het nog wel lastig vind om te bepalen welke informatie in welk markdown bestand hoort.


### 'Biggest decision'
Voor mij was het gebruiken van een Custom User model de grootste knoop om door te hakken. Deze keuze moest helemaal aan het begin gemaakt worden, aangezien een Custom User model vóór de eerste migrate aanwezig moet zijn. Dit lukte helaas niet in één keer (ook niet in vijf keer), waardoor ik meerdere keren het hele project heb moeten verwijderen en opnieuw heb moeten beginnen. Ik heb gekozen om met een Custom User model te werken, omdat ik graag extra gegevens van een gebruiker wilde opslaan, zoals adresgegevens en een geboortedatum. Ik had er ook voor kunnen kiezen en een extra model te maken en dit door middel van een ForeignKey te koppelen aan het normale User model van Django, maar ik wilde het graag 'echt' doen. Uiteindelijk is het gelukt en hier ben ik dan ook trots op.