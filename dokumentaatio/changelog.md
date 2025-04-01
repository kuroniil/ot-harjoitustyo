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