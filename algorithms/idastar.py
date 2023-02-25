from datastructs.solmu import Solmu
from datastructs.graph import Graph
from algorithms.algoritmi import Algoritmi
from math import sqrt

class IdaStar(Algoritmi):
    def __init__(self, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph, visualisoi=False, tarkkailija=None):
        self.alku_x, self.alku_y, self.loppu_x, self.loppu_y = alku_x, alku_y, loppu_x, loppu_y
        self.verkko = verkko
        self. max_h = verkko.hae_pituus() - 1
        self.max_w = verkko.hae_leveys() - 1
        self.alku: Solmu = verkko.hae_solmu(alku_x, alku_y)
        self.loppu: Solmu = verkko.hae_solmu(loppu_x, loppu_y)
        self.polku = []

    def runko(self):
        """
        Runkosilmukka rekursiiviselle syvyyshaulle. 
        """
        alku = self.alku
        maali = self.loppu
        if self.on_mahdoton(alku, maali):
            return {"etäisyys":float("inf"), "reitti":[]}
        yläraja = self.heuristiikka(alku)
        polku = self.polku
        polku.append(alku)
        while True:
            hakutulos = self.rekursiivinen_haku(alku, yläraja, 0, polku) # Etäisyys itseensä on 0
            if hakutulos == float("inf"):
                return {"etäisyys":float("inf"), "reitti":[]}
            elif hakutulos == "MAALI":
                return {"etäisyys":yläraja, "reitti":polku}
            yläraja = hakutulos

    def rekursiivinen_haku(self, solmu: Solmu, yläraja, etäisyys, polku):
        """
        Rekursiivinen syvyyshaku, joka käsittelee solmuja jos niiden etäisyysarvio
        """
        #solmu = polku.pop()
        etäisyysarvio = etäisyys + self.heuristiikka(solmu)
        if etäisyysarvio > yläraja:
            return etäisyysarvio
        if (solmu.get_koordinaatit() == (self.loppu_x, self.loppu_y)):
            return "MAALI"
        minimi = float("inf")
        for naapuri in solmu.get_naapurit():
            #if naapuri not in(polku):
            naapurisolmu, etäisyys_naapuriin = naapuri
            #polku.append(naapurisolmu)
            hakutulos = self.rekursiivinen_haku(naapurisolmu, yläraja, etäisyys + etäisyys_naapuriin, polku)
            if hakutulos == "MAALI":
                return hakutulos
            if hakutulos < minimi:
                minimi = hakutulos
            #polku.pop()
        return minimi

    def on_mahdoton(self, alku, loppu):
        """Ottaa alku- ja maalisolmun. Palauttaa True jos ne ovat estettyjä tai rajojen ulkopuolella"""
        if isinstance(alku, int) or isinstance(loppu, int):
            return True
        ax, ay = alku.get_koordinaatit()
        lx, ly = loppu.get_koordinaatit()
        return False


    def aloita(self):
        return self.runko()

    def heuristiikka(self, solmu):
        """
        Karsivana etäisyytenä käytetään oktiilietäisyyttä (octile distance)
        Soveltuu lukuisista etäisyysarvioista parhaiten tilanteeseen, jossa voidaan liikkua diagonaalisesti
        """
        x, y = solmu.get_koordinaatit()
        dx = (abs(x - self.loppu_x))
        dy = (abs(y - self.loppu_y))
        # Ortogonaalinen etäisyys on 1, diagonaalinen sqrt(2)
        etäisyysarvio = (1 * (dx + dy) + (sqrt(2) - 2) * min(dx, dy))
        return etäisyysarvio

