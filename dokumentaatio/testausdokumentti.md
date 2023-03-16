## Testikattavuus 

![Testikattavuus](https://raw.githubusercontent.com/miartris/Dijkstra-vs-IDA-/main/tests/test_cov_updated.png)

## Mitä testattiin

### Tietorakenteet

*Binäärikeko* 
Lisäys ja poisto-operaatioita on testattu tilanteessa, jossa keko on tyhjä tai solmu ei ole validi ja muuten lisäämällä/poistamalla
satunnainen määrä lukuja per testikerta ja varmistamalla, että poistetut ja lisätyt alkiot todella ovat pienimpiä alkioita ja että
kekorakenne on eheä

*Tiedostokäsittelijä*
Varmistettiin, että testidatan ja karttojen parseri palauttaa halutunlaista dataa tarkastamalla mittasuhteita ja vertaamalla
toivotunlaiseen syötteeseen

### Algoritmit

Dijkstran algoritmin erikoistapaukset, missä reitti on alkusolmuun itseensä, reitti on rajojen ulkopuolella ja reittiä ei ole testattu.
Lisäksi testattu, että etäisyydet lasketaan oikein kartalla, jossa joudutaan liikkumaan pahimmillaan kahdeksaan suuntaan vertaamalla
tunnettuihin benchmarkkeihin.

IdaStarista on testattu samat erityistapaukset ja testattu oikeita etäisyyksiä vertaamalla niitä dijkstran vastaaviin etäisyyksiin samalla kartalla.
Etäisyyksien maksimipituus on tosin pienempi, sillä algoritmin aikavaativuus on eksponentiaalinen

### Vertailu

Suorituskykyä testattiin erillisellä moduulilla, jossa alustettiin ensin kartta ja mitattiin aikaa nanosekunneissa noin 2000 kertaa dijkstralla ja vähemmän ida*:lla
neljällä eri kartalla suurenevilla syvyyksillä [tässä](https://github.com/miartris/Dijkstra-vs-IDA-/blob/main/tests/benchmark_20230316-200329.csv). Huomataan, että varsinkin Dijkstra noudattaa hyvin aikavaativuuksia. Ida* tuloksissa on paljon varianssia, lyhyilläkin etäisyyksillä se voi joutua käsittelemään todella monta solmua 
mikäli se jää kiinni esteisiin, milloin minimietäisyysarviota kasvatetaan ja mahdollisia ratkaisupolkuja syntyy eksponentiaalinen määrä lisää
