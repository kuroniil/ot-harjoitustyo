# Viikko 2

- Alustava määrittelydokumentti toteutettu

# Viikko 3

- Lisätty käyttöliittymä, jossa päävalikko toteutettu
- Aloitettu pelin käyttöliittymä
- Alustavat luokat sovelluksen käyttöliittymälle:
    * Pääluokka UI
    * Luokka MainMenu, jonka nappien avulla pääsee eri osiin sovellusta
    * Luokka Game, joka vastaa pelin elementtien näyttämisestä kuten ruudukon eri värisistä paloista
- Aloitettu luokka GameLogic, joka vastaa pelin logiikasta, kuten ruudukon liikkeestä move-metodilla
- GameLogic ruudukon liike testattu
- Käyttöliittymä yhdistetty pelilogiikkaan antamalla Game-luokalle GameLogic instanssi

# Viikko 4
- Pelin ruudukon liike toteutettu puuttuviin suuntiin
    * Alustava logiikka toteutettu - vaatii vielä refaktorointia
- Lisätty tulos peliin
    * Tulos kasvaa yhdistetyn palan määräämällä numerolla
        * esim. kaksi 4-palaa yhdistetään --> tulos kasvaa 4:llä
- Lisätty pelin päättymisen logiikka
    * Tilanteessa, jossa peli on lähellä päättyä, luodaan uusia GameLogic instansseja, jossa "simuloidaan" mitä
    tapahtuisi (päättyisikö peli) kaikilla eri siirroilla (ylös, alas, vasemmalle oikealle)
- Lisätty pelin päättymisnäkymän elementit Game luokkaan
    * Ilmoitusteksti pelin päättymisestä
    * Tuloksen tallentamislomake
        * Tuloksen tallentaminen ei vielä toteutettu
- Uuden pelin aloitus r-näppäimellä
- Otettu pylint käyttöön

# Viikko 5
- Lisätty pelin tuloksen tallennus tietokantaan
    * Käyttäjä saa tiedon lisäyksen onnistumisesta
    * Saman tuloksen voi lisätä vain kerran
      * Tämän jälkeen tulee aloittaa uusi peli tai palata päävalikkoon
- Lisätty näkymä, jossa vanhoja tallennettuja tuloksia voi tarkastella
    * Käyttäjä voi valita minkä pelimuodon tuloksia tarkastelee
    * Yhdellä sivulla näkyy taulu viidestä tuloksesta kerrallaan ja seuraaviin pääsee aina napilla
    * Järjestetty tuloksen mukaan
- Lisätty moduuli tietokantaan yhdistämistä varten, sekä tietokannan alustamisskripti
- Lisätty luokat, joiden avulla edellä kuvatut ominaisuudet toteutetaan
    * Leaderboard - näkymä tuloksille
    * Scores ja Score - Score on olio tietokannan scores taululle. Scores käsittelee Score-olioita, järjestää niitä yms.
- Refaktoroitu Grid luokan ruudukon liikkumista ja törmäyksiä
- Lisätty testejä Grid luokan ruudukon liikkumiselle

# Viikko 6
- Lisätty pelin tallennus tietokantaan
    * Käyttäjä voi jatkaa peliä tallennetusta kohdasta
    * Pelin ruudukko, tulos ja päivämäärä tallennetaan
- Lisätty näkymä, josta tallennetuja pelejä voi tarkastella ja jatkaa
    * Listattu päivämäärän ja tuloksen mukaan
    * Lajiteltu id:n mukaan, jotta uusin näkyy ensimmäisenä
    * Käyttäjä pystyy jatkaa tallennettua peliä klikkaamalla peliä
- Lisätty 5x5 ruudukon pelimuoto
    * Kaikki ominaisuudet toimii molemmilla pelimuodoilla
- Lisätty testejä
    * Tuloksen tallentaminen tietokantaan
      * Käytössä erillinen testitietokanta, kun testit ajetaan invoken kautta tai APP_ENV ympäristömuuttuja asetetaan manuaalisesti 
    * Tallennetun pelin jatkaminen pelilogiikan osalta
