```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Monopolipeli -- Vankila
    Monopolipeli -- Aloitusruutu
    Pelilauta "1" -- "40" Ruutu
    Aloitusruutu "1" --|> Ruutu
    Vankila "1" --|> Ruutu
    Sattuma_ja_yhteismaa "6" --|> Ruutu
    Asemat_ja_laitokset "6" --|> Ruutu
    Kadut "22" --|> Ruutu
    Kadut -- "0..4" Talot
    Kadut -- "0..1" Hotellit
    Sattuma_ja_yhteismaa -- Kortit
    Kortit -- Toiminto
    Ruutu -- Toiminto
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Kadut -- Pelaaja
    Rahat -- Pelaaja
```