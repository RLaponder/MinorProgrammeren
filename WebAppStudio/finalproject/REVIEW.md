# Final project - code review

## Feedback van mijn partner (Kay Brouwers)
* Wat meer werken met models en relationships tussen de models.
Mijn models zijn op dit moment nog vrij simpel. Door nog een aantal models toe te voegen en relationships zoals ManyToMany toe te voegen, zou me dit vrij eenvoudig relatief veel functionaliteit kunnen geven. 
Bijvoorbeeld:
    * Een 'gebouw' model toevoegen, waarmee ik kan controleren of iemand een juiste combinatie van gebouw en verdieping heeft ingevoerd.
    * Een 'categorie' model toevoegen, die vervolgens aan activiteit wordt gelinkt. Op dit moment is 'categorie' nog een attribute van een activiteit. Door er een eigen model van te maken, heb ik als admin meer invloed op de input.
* Meer enters tussen lange stukken code.
In views.py staan soms lange stukken code, die wel bij elkaar hoort, maar wellicht overzichtelijker zouden zijn wanneer er meer gebruik wordt gemaakt van witregels.
* Op dit moment worden alle activiteiten op de webpagina gesorteerd op datum weergegeven. Wanneer een activiteit is geweest, zal deze bovenaan blijven staan. Op een of andere manier zou ervoor gezorgd moeten worden dat deze activiteiten helemaal niet meer worden weergegeven, of bijvoorbeeld op een speciale pagina.
* Comments.
    * Over het algemeen is de code duidelijk en goed te volgen. Door het regelmatig gebruik van comments wordt duidelijk wat elk stukje code precies doet. Ik moet er wel opletten dat ik niet te veel comments plaats. Op sommige plaatsen staat er bijvoorbeeld een comment boven een enkele regel code en tenzij het om een hele complexe regel gaat, is dit niet nodig.

## Wat ik zelf nog graag zou aanpassen/toevoegen
Ik ben het eens met de feedback die ik heb gekregen van mijn partner, en ik zou mijzelf waarschijnlijk dezelfde feedback hebben gegeven. De reden waarom ik de dingen op deze manier heb gedaan, zijn voor een groot deel te wijten aan de relatief korte tijd. De comments en enters zijn naar mijn mening ook een kwestie van persoonlijke stijl, maar ik zal er in het vervolg beter op letten en er zorgvuldiger mee omgaan. 

#### Wanneer ik meer tijd zou hebben voor deze opdracht, zou ik graag nog functionaliteit willen toevoegen
* Zoekfunctie waarmee gezocht kan worden naar activiteiten met een bepaalde naam, of activiteiten binnen een bepaalde categorie.
* Zoekfunctie waarmee gezocht kan worden naar andere bewoners en hun profiel en de activiteiten die zij hebben gecreëerd kan bekijken.
* Per activiteit kan iedereen zien wie zich heeft aangemeld.
* Bij het creëren van een activiteit kan gekozen worden voor het 'thuisadres' van de gebruiker, zodat niet het hele adres ingevoerd moet worden.
* Bewoners kunnen berichten plaatsen onder een activiteit.
* Wanneer iemand een mail heeft gehad met een overlast-bericht, kan de persoon hier op reageren.
* Het hele register form controleren door middel van javascript. Op dit moment wordt alleen gecontroleerd of e-mail adress en wachtwoorden ingevoerd zijn en overeenkomen.
* Alle adressen van het complex toevoegen aan de database en bij het registreren controleren of het ingevoerde adres overeenkomt met een van de adressen in de database.
* Bewoners laten inloggen met hun e-mail, zodat het hebben van een gebruikersnaam niet meer nodig is.
* Bewoner kan zijn/haar eigen activiteiten aanpassen nadat ze zijn ingediend.

Vooraf dacht ik dat het **werken met een overlast-knop** en **werken me de database** de grootste valkuilen zouden zijn. Achteraf viel dit mee. Het bleek vrij simpel om met Django een mail te versturen. Daarnaast viel het werken met de database ook mee. Als ik wat meer tijd had gehad, had ik me wel graag meer willen verdiepen in de verschillende relaties die models onderling kunnen hebben, aangezien ik het nu vrij simpel heb gehouden.
