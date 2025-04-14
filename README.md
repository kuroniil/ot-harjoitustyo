# Ohjelmistotekniikka harjoitustyö

## Yleistä

Sovellus on Tkinterillä toteutettu 2048 peli, jossa ruudukkoa liikutetaan näppäimistöllä. Sovelluksessa käyttäjä voi pelata ja tallentaa tuloksiaan tietokantaan paikallisesti. Tulokset tallentuu pelimuodon mukaan ja niitä voi tarkastella järjestettynä niille tarkoitetulla sivulla.

# Käyttöohjeet

## Käynnistysohjeet

Asenna sovelluksen riippuvuudet komennolla ```poetry install```

Ensimmäisellä kerralla käynnistäessä tietokanta tulee alustaa. Sen voi tehdä komennolla ```poetry run invoke db-init```

Nyt voit käynnistää sovelluksen ```poetry run invoke start```

## Testit

Sovelluksen testit voi ajaa komennolla ```poetry run invoke test```

Coverage-testikattavuusraportin saa generoitua komennolla ```poetry run invoke coverage-report```

## Pylint

Pylint-tarkastukset koodille saa suoritettua komennolla ```poetry run invoke lint```

## Release

<a href=https://github.com/kuroniil/ot-harjoitustyo/releases/tag/viikko5>Sovelluksen uusin versio</a>

## Dokumentaatio

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md>Tuntikirjanpito</a>

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md>Vaatimusmäärittely</a>

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md>Changelog</a>

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md>Arkkitehtuuri</a>
