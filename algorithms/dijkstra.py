from datastructs.solmu import Solmu
from datastructs.graph import Graph
# Käyttää tilapäisesti valmista kekoa. Korvataan myöhemmin omalla toteutuksella
import heapq

class Dijkstra:
    
    def __init__(self, alku, loppu, verkko, visualisoi: bool):
        self.alku = alku
        self.loppu = loppu
        self.verkko = verkko
        self.visualisoi = visualisoi
        self.etäisyysmatriisi = [[float("inf") for _ in range(len(verkko))] for _ in range(len(verkko))]
        self.vierailtu = [[False for _ in range(len(verkko))] for _ in range(len(verkko))]
        self.keko = []
        self.lyhin_polku()
    
    def lyhin_polku(self):
        self.etäisyysmatriisi[self.alku] = 0
        heapq.heappush(self.keko, (self.alku, 0))
        while len(self.keko) > 0:
            käsiteltävä_solmu, etäisyys = heapq.heappop(self.keko) # 
            x, y = käsiteltävä_solmu.get_koordinaatit()
            if self.vierailtu[x][y]:
                continue
            self.vierailtu[x][y] = True
            for naapuri in käsiteltävä_solmu.get_naapurit():
                naapurisolmu, etäisyys_naapuriin = naapuri
                nx, ny = naapurisolmu.get_koordinaatit()
                nykyetäisyys = self.etäisyysmatriisi[nx][ny] 
                uusi_etäisyys = self.etäisyysmatriisi[x][y] + etäisyys_naapuriin
                if uusi_etäisyys < nykyetäisyys:
                    heapq.heappush(self.keko, (naapurisolmu, uusi_etäisyys))
                    self.etäisyysmatriisi[nx][ny] = uusi_etäisyys
    

        