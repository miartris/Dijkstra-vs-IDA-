import os
from re import findall


class Tiedostokäsittelijä:

    def __init__(self, tiedostopolku=None, kansiopolku=None, testipolku=None) -> None:
        self.tiedostopolku = tiedostopolku 
        self.kansiopolku = kansiopolku
        self.testipolku = testipolku

    def käsittele_karttatiedostot(self):
        kartat = []
        if self.kansiopolku:
            for tiedosto in os.listdir(self.kansiopolku):
                tiedostopolku = os.path.join(self.tiedostopolku, tiedosto)
                with open(tiedostopolku, "r") as f:
                    kartat.append(self.parse_kartta(f.readlines()))
        return kartat

    def käsittele_karttatiedosto(self):
        if self.tiedostopolku:
            with open(self.tiedostopolku, "r") as f:
                karttamatriisi = self.parse_kartta(f.readlines())
        return karttamatriisi

    def parse_kartta(self, kartta: list) -> dict:
        # Korkeus indeksissä 1 leveys indeksissä 2
        height, width = [int (val) for val in findall(r'\d+', kartta[1] + kartta[2])]
        # Älä sisällytä viimeistä tyhjää riviä
        raaka_karttadata = kartta[4:len(kartta)]
        # Poista \n merkkijonojen perästä
        karttadata = [jono.strip() for jono in raaka_karttadata]
        return {"korkeus":height, "leveys":width, "karttadata":karttadata}

    def parse_testi(self):
        testit = []
        if self.testipolku:
            with open(self.testipolku, "r") as f:
                testidata = f.readlines()
                relevantti_data = testidata[1:]
                puhdistettu_data = [jono.strip() for jono in relevantti_data]
                # Luo dict-oliot datasta
                for jono in puhdistettu_data:
                    alkiot = jono.split()
                    relevantit_alkiot = alkiot[1:]
                    for ind in range(len(relevantit_alkiot)):
                        if ind > 0 and ind < len(relevantit_alkiot) -1:
                            relevantit_alkiot[ind] = int(relevantit_alkiot[ind])
                        elif ind == len(relevantit_alkiot) -1:
                            relevantit_alkiot[ind] = float(relevantit_alkiot[ind])     
                    avaimet = ["kartta", "w", "h", "x1", "y1", "x2", "y2", "etäisyys"]
                    testiolio = {avaimet[i]:relevantit_alkiot[i] for i in range(len(relevantit_alkiot))}
                    testit.append(testiolio)
        return testit


