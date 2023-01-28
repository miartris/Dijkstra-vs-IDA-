# Määrittelydokumentti

## Projekti

Projektin tarkoituksena on vertailla Dijkstran ja IDA* reitinhakualgoritmien tehokkuutta keskenään esimerkiksi videopelikartoilla.
Vertailun tueksi toteutetaan algoritmin suorituksenaikainen graafinen visualisointi.

### Syöte

Testisyötteenä käytetään esim. [moving ai lab:in](https://movingai.com/benchmarks/grids.html) 2D karttoja, mitkä mahdollistavat rajojen\
sisällä liikkumisen kahdeksaan viereiseen ruutuun tietyin ruutukohtaisin ehdoin. Pääilmansuuntiin liikkumisen hinta on *yksi* diagonaalisesti $\sqrt{2}$

Näille kartoille on määritetty testejä lyhimmälle reitille lähtöpikselistä (x, y) maalipikseliin (x<sub>1</sub>, y<sub>1</sub>).
Toteutettujen algoritmien tulisi löytää juuri tämä reitti ja etäisyyden tulee täsmätä todellisen etäisyyden kanssa. 

### Algoritmit ja tietorakenteet

Tarvittavista tietorakenteista Dijkstran algoritmin prioriteettijono toteutetaan itse. IDA* käyttää valmiita tietorakenteita. Taulukon sijaan 
prioriteettijonolla toteutettu Dijkstra on aikavaativuudeltaan paljon tehokkaampi.

## Muu tieto 

Ohjelmointikieli ja versio: Python 3\
Opinto-ohjelma: TKT\
Projektin kieli: Suomi

