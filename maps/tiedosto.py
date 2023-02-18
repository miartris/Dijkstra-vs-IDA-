import os
from re import findall


class Tiedostokäsittelijä:

    def __init__(self, tiedostopolku) -> None:
        self.tiedostopolku = tiedostopolku 

    def käsittele_tiedostot(self):
        kartat = []
        for tiedosto in os.listdir(self.tiedostopolku):
            tiedostopolku = os.path.join(self.tiedostopolku, tiedosto)
            with open(tiedostopolku, "r") as f:
                kartat.append(self.parse_kartta(f.readlines()))
        return kartat

    def käsittele_tiedosto(self):
        with open(self.tiedostopolku, "r") as f:
            karttamatriisi = self.parse_kartta(f.readlines())
        return karttamatriisi

    def parse_kartta(self, kartta: list):
        # Korkeus indeksissä 1 leveys indeksissä 2
        height, width = [int (val) for val in findall(r'\d+', kartta[1] + kartta[2])]
        # Älä sisällytä viimeistä tyhjää riviä
        raaka_karttadata = kartta[4:len(kartta)]
        # Poista \n merkkijonojen perästä
        karttadata = [jono.strip() for jono in raaka_karttadata]
        return {"korkeus":height, "leveys":width, "karttadata":karttadata}

    def parse_testi():
        pass

        










