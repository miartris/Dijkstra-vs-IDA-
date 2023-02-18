# Etsi lyhin etäisyys alku- ja loppukoordinaatin välillä 2D-matriisissa

from datastructs.solmu import Solmu
from datastructs.graph import Graph
# Käyttää tilapäisesti valmista kekoa. Korvataan myöhemmin omalla toteutuksella
import heapq

class Dijkstra:

    def __init__(self, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph, visualisoi=False, init_olio=None):
        self.alku_x, self.alku_y, self.loppu_x, self.loppu_y = alku_x, alku_y, loppu_x, loppu_y
        self.alku: Solmu = verkko.hae_solmu(alku_x, alku_y)
        self.loppu: Solmu = verkko.hae_solmu(loppu_x, loppu_y)
        self.verkko = verkko
        self.visualisoi = visualisoi
        self.etäisyysmatriisi = [[float("inf") for _ in range(verkko.hae_leveys()) ] for _ in range(verkko.hae_pituus())]
        self.vierailtu = [[False for _ in range(verkko.hae_leveys())] for _ in range(verkko.hae_pituus())]
        self.keko = []
        self.lyhin_reitti = []
        self.lyhin_polku()
        # Yhdistää ylläolevia parametrejä olioon. Todo
        if init_olio:
            pass
    
    def lyhin_polku(self):
        lisäysindeksi = 0 # Jos keossa on samoja etäisyyksiä poistetaan ekana lisätty
        self.etäisyysmatriisi[self.alku_x][self.alku_y] = 0
        heapq.heappush(self.keko, (0, lisäysindeksi, self.alku))
        while len(self.keko) > 0:
            käsiteltävä_solmu = heapq.heappop(self.keko)[2]  
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
                    self.etäisyysmatriisi[nx][ny] = uusi_etäisyys
                    lisäysindeksi += 1
                    naapurisolmu.set_edeltäjä(käsiteltävä_solmu)
                    kolmikko = (uusi_etäisyys, lisäysindeksi, naapurisolmu)
                    heapq.heappush(self.keko, kolmikko)
                    
    def get_lyhin_polku(self):
        return self.etäisyysmatriisi[self.loppu_x][self.loppu_y]

    # Palauttaa lyhimmän reitin koordinaattiparit. Sisältää alku- ja loppusolmun
    def get_lyhin_reitti(self):
        self.alku.set_edeltäjä(None)
        if len(self.lyhin_reitti) < 1:
            nyky = self.loppu
            self.lyhin_reitti.append(self.loppu.get_koordinaatit())
            while True:
                edeltäjä = nyky.get_edeltäjä()
                if edeltäjä:
                    self.lyhin_reitti.append(edeltäjä.get_koordinaatit())
                    nyky = edeltäjä
                else: 
                    self.lyhin_reitti.reverse()
                    break
        return self.lyhin_reitti
    
    
    


        