# 2586

## 1. Pelin kehitys
2586 on Metropolian tieto- ja viestintätekniikan ensimmäisen vuoden opiskelijoiden suunnittelema ja itse koodaama peli valmiista tietokannasta.
Pelin tekijät:
Miia Laaksonen, 
Sofia Järvelä, 
Anni Saarelma, 
ja Rosamari Hautala

## 2. Kuvaus pelistä
Peli perustuu vuoteen 2586, jolloin alienit ovat valtaamassa maapallon ja uhkaavat levittävät tappavaa virusta. Pelissä pelaajan täytyy hakea toiselta puolelta maailmaa muinainen ainesosa, jota voidaan käyttää vastalääkkeen valmistamiseen. Pelaaja liikkuu maasta toiseen lentämällä, mutta lentokentillä odottaa aina erilaisia ratkaistavia tehtäviä. Tehtävän suoritus määrittää, miten peli jatkuu. Pelaajalla on tietty määrä valuuttaa sekä välimatkaa perässä kulkeviin alieneihin. Tarkoitus on päästä pelin alkupisteestä Kuubasta Norjaan ja takaisin niin, että alienit eivät saa kiinni tai valuutta ei lopu kesken. Pelissä on huomioitu kestävä kehitys, sillä pelaaja lentää sähkökäyttöisellä lentokoneella, joka vähentää lentopetrolin käyttöä ja vähentää kasvihuonepäästöjä.
## 3. Tarvittavat muutokset tietokannassa
Peliä varten tarvitaan tietokantaa lentokonepelistä. Tietokanta kuitenkin sisältää turhaa infoa, sekä  sinne täytyy lisätä mm. taulukko välimatkaa ja valuuttaa varten. 
Tarvittavat muutokset:
1. CO2- sarakkeen poistaminen : ALTER TABLE game DROP COLUMN co2_consumed, DROP COLUMN co2_budget;
2. Muutokset lentokenttiin :
* DELETE FROM airport WHERE type='seaplane_base';
* DELETE FROM airport WHERE type='closed';
* DELETE FROM airport WHERE type='heliport';
* DELETE FROM airport WHERE type='small_airport';
* DELETE FROM airport WHERE type='medium_airport';
- Kuubaan ja Norjaan jätetään vain aloitus- ja päämäärä- lentokentät
* DELETE FROM airport WHERE ident = 'ENBR';
* DELETE FROM airport WHERE ident = 'ENTC';
* DELETE FROM airport WHERE ident = 'ENVA';
* DELETE FROM airport WHERE ident = 'ENZV';
* DELETE FROM airport WHERE ident = 'MUVR';
4. Valuutan ja välimatkan lisääminen game- tauluun : ALTER TABLE game ADD COLUMN currency INT, ADD COLUMN alien_distance INT;
5. Tieto siitä, onko pelaajalla muinainen ainesosa mukana : ALTER TABLE game ADD COLUMN in_possession BOOLEAN;


Alla kuva muokatusta game- taulusta.
![image](https://github.com/seitamnn/MAAILMANLOPUNPELI/assets/156774906/7f4a5371-cbe0-4baf-a4bd-435a620117a7)

## 4. Miten peli toimii?
Peli toteutetaan Python-kielellä, sekä se käyttää muokattua relaatiotietokantaa. Se on tehty pelattavaksi näppäimistöllä.
Liikkuminen lentokenttien välillä toimii niin, että ohjelma arpoo pelaajalle kolme eri lentokenttää, joista pelaaja valitsee mieluisimman vaihtoehdon. 
Tietokantaan on määrätty tietty määrä etäisyyttä sekä valuuttaa, jotka lisääntyvät tai vähenevät pelin edetessä. Jokaisen tehtävän jälkeen tietokanta päivittyy pelaajan suorituksen mukaan. Osassa tehtävissä pelaajalla on mahdollisuus valita kahden vaihtoehdon väliltä, mutta joissakin lopputulos määräytyy sen mukaan, vastaako pelaaja oikein vai väärin esimerkiksi laskutehtäviin. 
