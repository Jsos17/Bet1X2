# Bet1X2App/Tietokantasovellus alkukesä 2018

## Laboratory work: Database application

### Bookmaker Bet1X2

Bet1X2 is a fictional bookmaker which offers only 1X2 type betting (the possible outcomes of a sporting event, for example a soccer match, are *a home win (1)*, *a draw (X)* or *an away win (2)*). Typically, this type of betting is offered in Europe for football (soccer) betting. 

This project was done for the University of Helsinki course *Laboratory work: Database application* during May and June of the year 2018. This was also the first project where I coded in Python.

The project consists of implementing the basic functionality of the website of the bookmaker Bet1X2. On Bet1X2's website, customers can create accounts, deposit or withdraw (fictional) money and, most importantly, place bets on 1X2 type events. Administrators can add matches and set the odds in such a way that the customer has no arbitrage opportunities. Instead, at least theoretically, the arbitrage is on the bookmaker's side.

The pricing of match outcomes (i.e. setting the odds) consists of the administrator assigning (subjective) probabilities for different outcomes 1, X and 2 (which must sum to 1). Then the odds are calculated in such a way that the expected profit of the bookmaker is 10 % from every bet. This holds, if the total amount of money wagered is distributed according to the assigned probabilities. For risk management purposes, a real bookmaker would potentially have to change the odds, if the total money wagered on the match was distributed significantly differently than the assigned probabilities. However, this functionality was not implemented in the project, since it would have been outside the scope of the course.

The goal of the course was to integrate a database to a web application, and to implement proper validation of forms. Therefore, the odds calculation mechanism was an extra feature from this vantage point, and significantly less time was spent on it. As a result, if the probability of an outcome (1, X or 2) is greater or equal to 90 %, then the odds have to be set manually, since this case is not handled automatically.


## Vedonvälittäjä Bet1X2

Vedonvälitystoimisto Bet1X2 tarjoaa pelkästään 1X2-tyyppisiä vetoja rekisteröityneille asiakkailleen internetsivullaan.

Asiakas voi rekisteröityä sivulla, ja sen jälkeen lyödä vetoa yhtiön tarjoamista otteluista. Ottelulla on kolme eri tulosmahdollisuutta: kotivoitto 1, tasapeli X ja vierasvoitto 2. Jokaiseen mahdollisuuteen liittyy kerroin ja tapahtuman todennäköisyys. Lisäksi otteluun liittyy kotijoukkue, vierasjoukkue, ajankohta ja myöhemmin varmistuva tulos. 

Bet1X2:n palautusprosentti on 90 % eli se ottaa laskennallisesti ja odotusarvoisesti 10 % jokaisesta ottelutapahtuman pelivaihdosta itselleen. Loput 90 % maksetaan pelaajille voittoina.

Vedonvälittäjällä työskentelee admin-oikeuksilla varustettuja henkilöitä, jotka voivat lisätä otteluita otteluvalikoimaan ja liittää niihin kotivoiton, tasapelin ja vierasvoiton todennäköisyyden. Otteluihin voidaan sitten liittää vetokohde, joka sisältää muun muassa kertoimet. Admin voi poistaa vetokohteen, jos siitä ei vielä ole lyöty vetoa. Muutoin admin voi vain muuttaa vetokohteen ei-aktiiviseksi tai sulkea sen.

Asiakas voi muuttaa salasanaansa ja lisätä saldoaan. Lisäksi asiakas voi poistaa tilinsä, jos hänellä ei ole avoimia vetoja, muulloin asiakas joutuu odottamaan, että avoimet vedot ratkeavat ja tämän jälkeen asiakas voi poistaa tilinsä. 

Asiakas ei voi perua vetoa sen jälkeen kun se on lyöty. Vedon lyötyään asiakas näkee mahdollisen voiton määrän. Asiakas voi lyödä useita vetoja samasta kohteesta (eri kupongeille).

Asiakas voi yhdistellä useita kohteita samaan vetokuponkiin. Asiakas voittaa, jos kaikki vetokupongin kohteet ovat oikein ja häviää muulloin paitsi jos kuponkiin liittyy mitätöity ottelu jolloin pelipanos palautetaan pelaajalle riippumatta muiden kohteiden tuloksesta.

Asiakas voi tarkastella vetohistoriaansa ja tarjolla olevia vetokohteita. Admin voi tarkastella kaikkien kohteiden vaihtoja ja käytettävissä olevien otteluiden listoja. Admin voi lisätä otteluita ja asettaa niiden tuloksen.

### Tietokannan rakenne

[Tietokantarakenne](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/tietokanta.md)

### Tietokantakaavio

[Bet1X2 tietokantakaavio](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/Bet1X2_tietokantakaavio.jpg)

### User stories

[User stories](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/user_stories.md)

### Toteutus, työn rajoitteet ja omat kokemukset

[Toteutus/rajoitteet/puutteet/kokemukset](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/rajoitteet_kokemukset.md)

### Asennusohje

[Asennusohje](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/asennusohje.md)

### Käyttöohje

[Käyttöohje](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/kaytto-ohje.md)

### Rekisteröity käyttäjä:

username: pelaaja1

password: 12345678

Tavallinen käyttäjä näkee pelkästään vetotarjoukset listana ja  voi lyödä vetoja niistä. Lisäksi käyttäjä näkee oman tilinsä, voi siirtää rahaa, vaihtaa salasanan ja poistaa tilinsä (ehdollisesti) sekä hän näkee pelihistoriansa. Käyttäjä voi myös etsiä vetokohteita joukkueen nimen tai sen osan perusteella

### Admin

Admin näkee: 
* ottelulistan, voi lisätä otteluita 

* voi lisätä vetokohteen (betting_offer) otteluun, jos otteluun ei vielä liity vetokohdetta, 

* näkee pelivaihdon (turnover statistics) ja rahan jakautumisen eri vaihtoehtojen kesken, 

* voi hallinnoida vetotarjouksia (Manage betting offers) esim. muuttamalla sen ei-aktiiviseksi jolloin kohde ei enää näy tavalliselle käyttäjälle 

* pelkällä admin-roolilla varustettu käyttäjä ei voi asettaa vetoja, eikä hän voi muokata tiliään, jotta joku ei käy vaihtamassa esimerkkitilin salasanaa tai poistamassa esimerkki-admintiliä

* admin voi asettaa ottelun tuloksen, mikä käynnistää tuloksesta riippuvien tietokohteiden päivityksen

### Huomioita

Jos tapahtuman todennäköisyys on 90 % tai yli niin kertoimet menevät alle 1:n johtuen puutteellisesta laskentamekanismista, ja tällöin kertoimia pitää säätää manuaalisesti jotta lomake validoidaan. 

* Kaikki toiminnallisuudet eivät näy esimerkiksi otteluun tai vetokohteisiin liittyen, koska esimerkiksi vetokohteen kertoimien muuttaminen, jos ottelu on jo ratkennut ei ole mielekästä, samoin tuloksen asetus useita kertoja jne
* Ottelun (sport_match) voi poistaa vain jos siihen ei liity vetokohdetta (betting_offer).
* Vetokohteen (betting_offer) voi poistaa, jos kohteesta ei ole lyöty vetoa
* Pelaaja voi poistaa tilin, jos hänellä ei ole avoimia vetoja
* Admin ei voi poistaa tiliä

