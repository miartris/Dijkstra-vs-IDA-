# Dijkstra vs IDA*

## Käyttö

### Riippuvuudet

Pythonista on käytössä versio 3. Projektiriippuvuudet voi asentaa suorittamalla juurihakemistossa komennon

```
pip install -r requirements.txt
```

Ohjelma käynnistyy avaamalla python3 tulkilla tiedoston main.py. Luultavasti jompi kumpi näistä
```
python3 main.py
py main.py
``` 
Ruudukon kokoa voi muuttaa.
Tällä hetkellä piirtotilan valittua voi hiirtä painamalla ja vetämällä valita alku- ja maaliruudun ja piirtää esteitä.
Tämän jälkeen algoritmin ollessa valittuna "aloita" nappia painamalla algoritmi määrittää lyhimmän polun. Polku visualisoidaan ja parin sekunnin päästä ruutu alustetaan uusiksi


### Testaus

Juurihakemistosta testit voi suorittaa komennolla 

```
pytest tests
```

Testikattavuuden ja testikattavuusraportin saa generoitua komennoilla

```
coverage run -m pytest tests
coverage report 
```

### Suorituskykytestaus

Suorittamalla ohjelman parametrillä -t 
```
py main.py -t
```
Ohjelma suorittaa suorituskykytestejä ja luo testikansioon csv tiedoston tyyliin benchmark_{timestamp}.csv

## Dokumentaatio
[Määrittelydokumentti](/dokumentaatio/määrittelydokumentti.md)\
[Viikkoraportit](/dokumentaatio/viikkoraportti1.md)\
[Testausdokumentti](/dokumentaatio/testausdokumentti.md)
[Toteutusdokumentti](/dokumentaatio/toteutusdokumentti.md)
