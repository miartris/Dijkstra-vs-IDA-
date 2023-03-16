## Yleisrakenne

Ohjelma koostuu graafisesta käyttöliittymästä, jossa käyttäjä voi valita xy kokoisella ruudukolla pisteitä, joiden välinen reitti etsitään. Ruudukkoon voi piirtää vapaasti esteitä. Polku visualisoidaan ja ruudukko tyhjennetään. Toinen osa on suorituskykytestaus, jossa käydään läpi noin 2000 reittiä kaikilla algoritmeilla neljällä eri videopelikartalla, jotka eroavat kooltaan ja esteiltään. 

Parannusehdotuksia on lukuisia. Esimerkiksi satunnaisen labyrintin generoiminen mm. Primin tai Kruskalin algoritmeillä, lisää ruututyyppejä ja enemmän kontrollia algoritmien suoritukseen ja visualisaatioon, tilastoja ratkaisun nopeudesta ja vierailtujen solmujen määrästä yms.

## Tietorakenteet

Algoritmeissa käytetään syötteenä verkkoa, joka on käytännössä vieruslistaesitys, joka
sisältää solmuja, jotka sisältävät tiedon omista naapureistaan ja etäisyyksistä niihin.

Verkot luodaan prosessoimalla lista merkkijonoja, joissa merkit kuvaavat vapaata tai blokattua ruutua.

Dijkstran algoritmissa pienimmän etäisyyden solmujen prosessoimiseen käytetään binäärikekoa. Koska 
ruudukossa etäisyyksiä on vain kaksi, syntyy runsaasti tilanteita joissa on useita yhtäsuuria minimietäisyyksiä.
Tasurit ratkotaan solmun lisäämisjärjestyksellä kekoon.

### Binäärikeko

Funktiot
- Add()
- Pop()
- Peek()
Binääripuurakennetta mallinnetaan implisiittisesti taulukolla indeksoidan 0:sta.

### Dijkstra

Dijkstra on toteutettu varsin perinteisesti. Ruudukossa etäisyyksien samankaltaisuudesta johtuen se alkukantaistuu
käytännössä leveyshauksi.

#### Aika- ja tilavaativuudet

Keko-operaatiot vievät logaritmisen määrän aikaa ja riippuvat solmujen ja kaarien määrästä. Pahimmillaan jokainen solmu on käytävä läpi,
jolloin jokainen solmu lisätään prioriteettijonoon ja poistetaan sieltä. Aikavaativuus on siis (E + log(V)), missä V on solmujen määrä ja E kaarien

Tilavaativuus on lineaarinen O(3V), sillä pidämme kirjaa yhdessä xy-kokoisessa matriisissa vierailusta, toisessa etäisyydestä ja lisäksi käytämme kekoa.

### IdaStar

Ida* on toteutettu perinteisesti. Pinorakenteena on tavallinen taulukko, joka hidastaa suoritusta kun tarkastamme onko solmu tämänhetkisessä rekursiossa
jo käsitelty. Toisaalta algoritmin hengessä tämä säästää kaikista eniten tilassa, sillä se on minimaalisin tietorakenne jolla saamme säilytettyä lyhimmän
polun solmut.

#### Aika- ja tilavaativuudet

Käsiteltävät verkot ovat varsin laajoja. Keskimäärin jokainen solmu haarautuu kahdeksaan suuntaan, ellei se ole kartan laidalla tai lähellä estettä.
Näin ollen Ida* saa syvyydessä d+1 noin 7 uutta mahdollista suuntaa, eli sen aikavaativuus on eksponentiaalinen b^d, missä b on todellinen haarautumiskeskiarvo
ja d ratkaisun syvyys.

Tilavaativuus on O(V), missä V on pahimassa tapauksessa verkon jokainen solmu, sillä pinossa säilytetään vain senhetkisen rekursion solmut

## Yhteenveto

Huomataan, että tutkimissamme verkoissa Dijkstra on huomattavasti nopeampi eikä vie mahdottomasti enempää tilaa kun polun etäisyys alkaa kasvaa. IDA* suorituisi paremmin tilanteessa, jossa verkko ei juuri haaraudu, mutta missä ratkaisun syvyys olisi suuri ja mahdollisesti tuntematon ja vaikeasti arvioitavissa.

Lähteet:
Kartat [Moving-ai lab](https://www.movingai.com/benchmarks/grids.html)
