# Vaatimusmäärittely

## Yleistä

Sovelluksessa käyttäjä pystyy pelaamaan 2048 peliä ja pitämään kirjaa parhaista tuloksistaan. Peliä pystyy pelaamaan eri kokoisilla ruudukoilla.

## Käyttöliittymäluonnos

Sovellus koostuu kolmesta eri päänäkymästä; päävalikko, peli ja tulokset.

![alt text](image.png)

Päävalikosta käyttäjä pystyy valita pelin eri kokoisilla ruudukoilla tai tulokset näkymän. Pelin päätyttyä pelinäkymään tulee ilmoitus pelin päättymisestä ja valikko vaihtoehdoista (päävalikkoon, uusi peli, tulokset).

## Sovelluksen toiminnallisuus

- Käyttäjä pystyy valitsemaan päävalikosta pelin eri kokoisilla ruudukoilla
    * Käyttäjä pystyy pelata nuolinäppäimillä
    * Pelissä pisteet määräytyy yhdistettyjen palikoiden perusteella
    * Tulos tallentuu pelin päätyttyä yhdistettynä ruudukon kokoon
- Käyttäjä pystyy tarkastelemaan aikaisempia pelien tuloksiaan tulokset sivulla
    * Ryhmitelty eri ruudukon kokojen perusteella
    * Lajiteltu parhaan tuloksen mukaan
    * Tuloksessa mukana nimimerkki
- Pelin päätyttyä käyttäjä voi valita pelata uudestaan, tarkastella tuloksia tai mennä päävalikkoon

## Jatkokehitysideoita 

- Lisää eri ruudukon kokoja
- Pelin ulkoasun personointi (ruudukon väri yms.)
- Julkisessa internetissä oleva api tarjoaa tulokset, jotka sovellus hakee ja näyttää käynnistäessä paikallisesti
    * Tulokset myös talletettaisiin verkon yli ja käyttäjät näkisivät muiden käyttäjien jakamat tulokset
