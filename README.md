# Bet1X2App/Tietokantasovellus alkukesä 2018

## Vedonvälittäjä Bet1X2

Vedonvälitystoimisto Bet1X2 tarjoaa pelkästään 1X2-tyyppisiä vetoja rekisteröityneille asiakkailleen internetsivullaan.

Asiakas voi rekisteröityä sivulla, ja sen jälkeen lyödä vetoa yhtiön tarjoamista otteluista. Ottelulla on kolme eri tulosmahdollisuutta: kotivoitto 1, tasapeli X ja vierasvoitto 2. Jokaiseen mahdollisuuteen liittyy kerroin ja tapahtuman todennäköisyys. Lisäksi otteluun liittyy kotijoukkue, vierasjoukkue, ajankohta ja myöhemmin varmistuva tulos. 

Bet1X2:n palautusprosentti on 90 % eli se ottaa laskennallisesti ja odotusarvoisesti 10 % jokaisesta ottelutapahtuman pelivaihdosta itselleen. Loput 90 % maksetaan pelaajille voittoina.

Vedonvälittäjällä työskentelee admin-oikeuksilla varustettuja henkilöitä, jotka voivat lisätä otteluita otteluvalikoimaan ja liittää niihin kotivoiton, tasapelin ja vierasvoiton todennäköisyyden. Otteluihin voidaan sitten liittää vetokohde, joka sisältää muun muassa kertoimet. Admin voi poistaa vetokohteen, jos siitä ei vielä ole lyöty vetoa. Muutoin admin voi vain muuttaa vetokohteen ei-aktiiviseksi tai sulkea sen.

Asiakas voi muuttaa salasanaansa ja lisätä saldoaan. Lisäksi asiakas voi poistaa tilinsä, jos hänellä ei ole avoimia vetoja, muulloin asiakas joutuu odottamaan, että avoimet vedot ratkeavat ja tämän jälkeen asiakas voi poistaa tilinsä. 

Asiakas ei voi perua vetoa sen jälkeen kun se on lyöty. Vedon lyötyään asiakas näkee mahdollisen voiton määrän. Asiakas voi lyödä useita vetoja samasta kohteesta (eri kupongeille).

Asiakas voi yhdistellä useita kohteita samaan vetokuponkiin. Asiakas voittaa jos kaikki vetokupongin kohteet ovat oikein ja häviää muulloin.

Asiakas voi tarkastella vetohistoriaansa ja tarjolla olevia vetokohteita. Admin voi tarkastella kaikkien kohteiden vaihtoja ja käytettävissä olevien otteluiden listoja. Admin voi lisätä otteluita ja asettaa niiden tuloksen.

### Alustava luokkakaavio

[Bet1X2 luokkakaavio](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/Bet1X2_luokkakaavio.jpg)

### Alustava tietokantakaavio

[Bet1X2 tietokantakaavio](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/Bet1X2_tietokantakaavio.jpg)

### User stories

[User stories](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/user_stories.md)

### Asennusohje

[Asennusohje](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/asennusohje.md)

### Käyttöohje

[Käyttöohje](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/kaytto-ohje.md)

### Rekisteröity käyttäjä:

username: pelaaja1

password: 12345678

Tavallinen käyttäjä näkee pelkästään vetotarjoukset listana ja  voi lyödä vetoja niistä. Lisäksi käyttäjä näkee oman tilinsä ja asetetut vetokupongit.

### Admin

username: hallinto

password: 12345678

Admin näkee: 
* ottelulistan, voi lisätä otteluita 

* voi lisätä vetokohteen (betting_offer) otteluun, jos otteluun ei vielä liity vetokohdetta, 

* näkee pelivaihdon (turnover statistics) ja rahan jakautumisen eri vaihtoehtojen kesken, 

* voi hallinnoida vetotarjouksia (Manage betting offers) esim. muuttamalla sen ei-aktiiviseksi jolloin kohde ei enää näy tavalliselle käyttäjälle 

* admin ei voi asettaa vetoja

* admin voi asettaa ottelun tuloksen, mikä käynnistää tuloksesta riippuvien tietokohteiden päivityksen

### Linkki herokuun

**HUOM Tietokantaan lisättiin taulut Role ja User_role (liitostaulu), ja tämän vuoksi kaikki herokun taulut poistettiin ma 25.6.2018 n. klo 04:13. Tämän vuoksi jotkin ohjeista voivat olla vanhentuneita (korjataan ennen loppudeadlinea)**

**HUOM** Kaikki taulut poistettiin ja asennettiin uudelleen pe 22.6.2018 n.~ klo 3.45, koska bet_coupon vierasavain bettor_id muutettiin: nullable=True, jotta pelaajan tilin poisto onnistuu ja kupongit jäävät olemassa oleviksi tietokantaan vierasavaimena NULL (python None)

**HUOM2** Salasanojen tallennus hashattuna 23.6.2018 n. klo 21:51, minkä johdosta herokun käyttäjätaulujen entryjä poistetaan ja luodaan uudelleen hashatyillä salasanoilla

**HUOM3 Adminin salasanan vaihto otettu pois käytöstä, jotta esimerkkitilin salasanaa ei pääse kukaan muuttamaan ja tilille pääsee**

[Bet1X2App](https://bet1x2-app.herokuapp.com/)

Huomioita:

Jos tapahtuman todennäköisyys on 90 % tai yli niin kertoimet menevät alle 1:n johtuen vielä puutteellisesta laskentamekanismista, ja tällöin kertoimia pitää säätää manuaalisesti jotta lomake validoidaan. 

* Ottelun (sport_match) voi poistaa vain jos siihen ei liity vetokohdetta (betting_offer).
* Vetokohteen (betting_offer) voi poistaa, jos kohteesta ei ole lyöty vetoa
* Admin ei voi poistaa tiliä (ainakaan vielä)

