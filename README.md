# 2586
## 1. Kuvaus pelistä
Peli perustuu vuoteen 2586, jolloin Alienit ovat vallanneet ihmiskunnan ja levittävät tappavaa virusta. Pelissä pelaajan täytyy hakea toiselta puolelta maailmaa muinainen ainesosa, jota voidaan käyttää vastalääkkeen valmistamiseen. Pelaaja liikkuu maasta toiseen lentämällä, mutta lentokentillä odottaa aina erilaisia ratkaistavia tehtäviä. Tehtävän suoritus määrittää, miten peli jatkuu. Pelaajalla on tietty määrä valuuttaa sekä välimatkaa perässä kulkeviin Alieneihin. Tarkoitus on päästä pelin alkupisteestä Kuubasta Norjaan ja takaisin niin, että Alienit eivät saa kiinni tai valuutta ei lopu kesken. 
## 2. Tarvittavat muutokset tietokannassa
Peliä varten tarvitaan tietokantaa lentokonepelistä. Tietokanta kuitenkin sisältää turhaa infoa, sekä  sinne täytyy lisätä mm. taulukko välimatkaa ja valuuttaa varten. 
Tarvittavat muutokset:
1. CO2- sarakkeen poistaminen : ALTER TABLE game DROP COLUMN co2_consumed, DROP COLUMN co2_budget;
2. Muutokset lentokenttiin :
* DELETE FROM airport WHERE type='seaplane_base';
* DELETE FROM airport WHERE type='closed';
* DELETE FROM airport WHERE type='heliport';
* DELETE FROM airport WHERE type='small_airport';
* DELETE FROM airport WHERE type='medium_airport';
4. Valuutan ja välimatkan lisääminen game- tauluun : ALTER TABLE game ADD COLUMN currency INT, ADD COLUMN alien_distance INT;
5. Tieto siitä, onko pelaajalla muinainen ainesosa mukana : ALTER TABLE game ADD COLUMN in_possession BOOLEAN;

Alla kuva muokatusta game- taulusta.
![image](https://github.com/seitamnn/MAAILMANLOPUNPELI/assets/156774906/7f4a5371-cbe0-4baf-a4bd-435a620117a7)

## 3. Miten peli toimii?
Peli toteutetaan Python-kielellä, sekä se käyttää muokattua relaatiotietokantaa. Se on tehty pelattavaksi näppäimistöllä. 
