# Tietokantarakenne

## Tietokantakaavio

![Bet1X2 tietokantakaavio](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/Bet1X2_tietokantakaavio.jpg)

[Linkki luokkakaavioon](https://github.com/Jsos17/Vedonlyonti1X2/blob/master/documentation/Bet1X2_luokkakaavio.jpg)

## Tietokanta

* Sport_match kuvaa ottelua
* Betting_offer kuvaa vedonlyöntikohdetta
* Bet_coupon kuvaa vedonlyöntikuponkia
* *Betting_offer_of_coupon* on liitostaulu *Bet_couponin* ja *Bettting_offerin* ja se kuvaa kupongin yksittäistä vetokohde-valintaa
* Bettor kuvaa käyttäjää (nimentä olisi voinut olla ehkä neutraalimpi user, koska myös adminia mallinnetaan tämän kautta)
* Role kuvaa rooleja, jotka voivat liittyä käyttäjään/pelaajaan. Oletuksena on olemassa roolit "CUSTOMER" ja "ADMIN" ja nämä entryt luodaan automaattisesti tietokantaan. Kuitenkin erillinen taulu mahdollistaa roolien laajentamisen tulevaisuudessa
* User_role on liitostaulu *Bettorin* ja *Role:n* välillä, eli on mahdollista että käyttäjään liittyy useampi rooli. Käytännössä kun asiakas luo tilin liitetään häneen "CUSTOMER" rooli ja muita rooleja ei sovelluksen kautta voi liittää. "ADMIN"-rooli voidaan asettaa komentorivin kautta, ja tällöin on suositeltavaa, että rooli "CUSTOMER" poistetaan, koska ADMIN ei tee mitään CUSTOMER-roolin oikeuksilla.

Tietokannassa on siis kaksi monesta-moneen suhdetta *Bettorin* ja *Role:n välillä*, sekä *Bet_couponin* ja *Bettting_offerin* välillä.

Täysi CRUD liittyy *Sport_matchiin*, *Betting_offeriin* ja *Bettoriin*, tietyin rajoituksin. Role ja User_role tauluja ei voi muokata sovelluksen kautta. 

*Sport_match* voidaan poistaa, jos siihen ei liity *Betting_offeria*, muokkauksessa tuloksen asetus on kertaalleen tehtävissä, muuten muokkausta ei ole rajoitettu, jos ottelu ei ole vielä ratkennut. 

*Betting_offer* voidaan poistaa, jos siihen ei liity *Betting_offer_of_couponeja* (ja siten myös *Bet_couponeja*) eli, jos vetokohteesta ei ole lyöty vetoa JA jos betting_offer on asetettu ei-aktiiviseksi. Kohdetta voi myös päivittää eli esimerkiksi kertoimia muuttaa. Kerroinmuutokset eivät vaikuta jo asetettuihin vetoihin, sillä jokaisen pelaajan "saama" kerroin on talletettu *Betting_offer_of_coupon* entryyn mallintaen todellisuutta.

*Bettor* vodaan poistaa (eli pelaaja voi poistaa tilinsä), jos kaikki hänen vetonsa ovat ratkenneet. Tällöin myös pelaajaan liittyvä User_role entry poistetaan, mutta sen sijaan kaikki pelaajaan littyvät vetokupongit jäävät olemaan olemassa, siten että niiden vierasavaimeksi tulee null. Päivitystoiminnallisuus liittyy salasanan vaihtoon ja tilin balanssin muuttamiseen rahansiirroilla, panoksien asettamisella ja voittojen saamisella. Jos bettorin rooli on pelkkä ADMIN ei tällainen käyttäjä pääse poistamaan tiliään sovelluksen kautta.

## Normalisointi

Tietokannan kaikki taulut ovat **ensimmäisessä normaalimuodossa**, koska:

* Minkään taulun sarake ei sisällä listoja
* Taulujen sarakkeet eivät muodosta toistuvia ryhmiä
* Sarakkeiden arvot ovat samantyyppisiä
* Jokaisessa taulussa sarakkeiden nimet ovat uniikkeja
* Sarakkeiden järjestys ei vaikuta tietokantataulun toimintaan
* Koska pääavaimet ovat kussakin taulussa uniikkeja, niin tauluissa ei voi olla kahta täsmälleen samanlaista riviä
* Rivien järjestys ei vaikuta tietokantataulun toimintaan

Tietokannan kaikki taulut ovat myös **toisessa normaalimuodossa**, koska jokaisen taulun pääavain on määritelty yhden sarakkeen avulla, ja koska taulut ovat ensimmäisessä normaalimuodossa.

Tietokannan **kaikki taulut paitsi Bet_coupon ja Bettor ovat myös kolmannessa normaalimuodossa**, sillä niiden sarakkeet eivät ole transitiivisesti riippuvaisia taulujen pääavaimesta. 

**Bet_coupon** taulussa *possible_win_eur* ja *possible_win_cent* ovat funktionaalisesti riippuvaisia sarakejoukosta *combined_odds*, *stake_eur* ja *stake_cent* ja näin ollen *possible_win_eur* ja *possible_win_cent* ovat myös transitiivisesti riippuvaisia taulun pääavaimesta. Tarkalleen ottaen voiton määriä ei välttämättä tarvitsisi tallentaa, mutta toisaalta tämä tilanne vähentää usein toistuvaa voiton uudelleen laskemista, tekee maksettavan voiton ja sen miten se pyöristetään yksiselitteiseksi, kun se kerran on laskettu, sekä helpottaa myös ohjelmointia.

**Bettor** taulussa username on uniikki, joten taulun kaikki muut sarakkeet ovat transitiivisesti riippuvaisia pääavaimesta. En kuitenkaan näe mitään hyötyä taulun pilkkomisesta pienempiin osiin, ja toisaalta käyttäjänimen uniikkiuden estäminen taas aiheuttaa tarpeettomia ongelmia. 

## Indeksointi

Erillisiä indeksejä ei ole asetettu, eli käytännössä vain avaimiin liittyy indeksi.

## CREATE TABLE -lauseet

	CREATE TABLE sport_match (
		id INTEGER NOT NULL, 
		home VARCHAR(144) NOT NULL, 
		away VARCHAR(144) NOT NULL, 
		prob_1 INTEGER NOT NULL, 
		prob_x INTEGER NOT NULL, 
		prob_2 INTEGER NOT NULL, 
		start_time DATETIME NOT NULL, 
		result_1x2 VARCHAR(4) NOT NULL, 
		PRIMARY KEY (id)
	);
	CREATE TABLE role (
		id INTEGER NOT NULL, 
		name VARCHAR(10) NOT NULL, 
		PRIMARY KEY (id), 
		UNIQUE (name)
	);
	CREATE TABLE bettor (
		id INTEGER NOT NULL, 
		username VARCHAR(144) NOT NULL, 
		password VARCHAR(144) NOT NULL, 
		balance_eur INTEGER NOT NULL, 
		balance_cent INTEGER NOT NULL, 
		PRIMARY KEY (id), 
		UNIQUE (username)
	);
	CREATE TABLE betting_offer (
		id INTEGER NOT NULL, 
		match_id INTEGER NOT NULL, 
		odds_1 FLOAT NOT NULL, 
		odds_x FLOAT NOT NULL, 
		odds_2 FLOAT NOT NULL, 
		max_stake FLOAT NOT NULL, 
		active BOOLEAN NOT NULL, 
		closed BOOLEAN NOT NULL, 
		PRIMARY KEY (id), 
		FOREIGN KEY(match_id) REFERENCES sport_match (id), 
		CHECK (active IN (0, 1)), 
		CHECK (closed IN (0, 1))
	);
	CREATE TABLE bet_coupon (
		id INTEGER NOT NULL, 
		bettor_id INTEGER, 
		combined_odds FLOAT NOT NULL, 
		stake_eur INTEGER NOT NULL, 
		stake_cent INTEGER NOT NULL, 
		possible_win_eur INTEGER NOT NULL, 
		possible_win_cent INTEGER NOT NULL, 
		bet_status VARCHAR(10) NOT NULL, 
		PRIMARY KEY (id), 
		FOREIGN KEY(bettor_id) REFERENCES bettor (id)
	);
	CREATE TABLE user_role (
		id INTEGER NOT NULL, 
		bettor_id INTEGER NOT NULL, 
		role_id INTEGER NOT NULL, 
		PRIMARY KEY (id), 
		FOREIGN KEY(bettor_id) REFERENCES bettor (id), 
		FOREIGN KEY(role_id) REFERENCES role (id)
	);
	CREATE TABLE betting_offer_of_coupon (
		id INTEGER NOT NULL, 
		betting_offer_id INTEGER NOT NULL, 
		bet_coupon_id INTEGER NOT NULL, 
		choice_1x2 VARCHAR(1) NOT NULL, 
		odds FLOAT NOT NULL, 
		status VARCHAR(10) NOT NULL, 
		PRIMARY KEY (id), 
		FOREIGN KEY(betting_offer_id) REFERENCES betting_offer (id), 
		FOREIGN KEY(bet_coupon_id) REFERENCES bet_coupon (id)
	);


