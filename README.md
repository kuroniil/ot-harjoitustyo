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

## Dokumentaatio

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/e4a49e005cf803e3b924151f0fa00241810825b6/dokumentaatio/tuntikirjanpito.md>Tuntikirjanpito</a>

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/e4a49e005cf803e3b924151f0fa00241810825b6/dokumentaatio/vaatimusmaarittely.md>Vaatimusmäärittely</a>

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/1c23567a6b6b8d6d9f8a6d95a6c8ffd542645f73/dokumentaatio/changelog.md>Changelog</a>

<a href=https://github.com/kuroniil/ot-harjoitustyo/blob/1a6a6e17efbc9d52a8cc47e677b7ff52e4c6282f/dokumentaatio/arkkitehtuuri.md>Arkkitehtuuri</a>
