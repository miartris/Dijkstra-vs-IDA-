from datastructs.solmu import Solmu
from datastructs.graph import Graph
from algorithms.algoritmi import Algoritmi
from datastructs.tila import Tila
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
        self.tarkkailija = tarkkailija
        if visualisoi:
            self.viive = 0.02

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
            hakutulos = self.rekursiivinen_haku(yläraja, 0, polku) # Etäisyys itseensä on 0
            if hakutulos == float("inf"):
                return {"etäisyys":float("inf"), "reitti":[]}
            elif hakutulos < 0:
                return {"etäisyys":yläraja, "reitti":polku}
            yläraja = hakutulos

    def rekursiivinen_haku(self, yläraja, etäisyys, polku):
        """
        Rekursiivinen syvyyshaku, joka käsittelee solmuja jos niiden etäisyysarvio
        """
        solmu = polku[-1]
        if (solmu.get_koordinaatit() == (self.loppu_x, self.loppu_y)):
            return -etäisyys
        etäisyysarvio = etäisyys + self.heuristiikka(solmu)
        if etäisyysarvio > yläraja:
            return etäisyysarvio
        solmu.muuta_tila(Tila.VIERAILLAAN)
        minimi = float("inf")
        if self.tarkkailija:
            self.puske_tila(solmu)
        for naapuri in solmu.get_naapurit():
            naapurisolmu, etäisyys_naapuriin = naapuri  
            if naapurisolmu not in(polku):
                polku.append(naapurisolmu)
                hakutulos = self.rekursiivinen_haku(yläraja, etäisyys + etäisyys_naapuriin, polku)
                if hakutulos < 0:
                    return hakutulos
                if hakutulos < minimi:
                    minimi = hakutulos
                s = polku.pop()
                s.muuta_tila(Tila.Vakio)
                if self.tarkkailija:
                    self.puske_tila(s)
        return minimi

    def on_mahdoton(self, alku, loppu):
        """Ottaa alku- ja maalisolmun. Palauttaa True jos ne ovat estettyjä tai rajojen ulkopuolella"""
        if isinstance(alku, int) or isinstance(loppu, int):
            return True
        ax, ay = alku.get_koordinaatit()
        lx, ly = loppu.get_koordinaatit()
        if (ax, ay) ==  (lx, ly):
            return True
        return False


    def aloita(self):
        tulos = self.runko()["reitti"]
        lista = [solmu.get_koordinaatit() for solmu in tulos]
        return lista
    
    def puske_tila(self, solmu: Solmu):
        alku = (self.alku_x, self.alku_y)
        loppu = (self.loppu_x, self.loppu_y)
        self.tarkkailija.päivitä_tila(solmu.get_koordinaatit(), solmu.get_tila(), [alku, loppu], self.viive)
        
    def heuristiikka(self, solmu):
        """
        Karsivana etäisyytenä käytetään oktiilietäisyyttä (octile distance)
        Soveltuu lukuisista etäisyysarvioista parhaiten tilanteeseen, jossa voidaan liikkua diagonaalisesti
        """
        x, y = solmu.get_koordinaatit()
        dx = abs(x - self.loppu_x)
        dy = abs(y - self.loppu_y)
        # Ortogonaalinen etäisyys on 1, diagonaalinen sqrt(2)
        etäisyysarvio = 1 * (dx + dy) + (sqrt(2) - 2) * min(dx, dy)
        return etäisyysarvio

