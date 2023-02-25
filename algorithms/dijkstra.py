# Etsi lyhin etäisyys alku- ja loppukoordinaatin välillä 2D-matriisissa

from datastructs.solmu import Solmu
from datastructs.graph import Graph
from algorithms.algoritmi import Algoritmi
# Käyttää tilapäisesti valmista kekoa. Korvataan myöhemmin omalla toteutuksella
import heapq

class Dijkstra(Algoritmi):
    """
    Laskee lyhimmän etäisyyden alkupisteestä loppupisteeseen ja sisältää metodin, millä saada listan reitin pisteistä.
    """
    def __init__(self, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph, visualisoi=False, tarkkailija = None):
        self.alku_x, self.alku_y, self.loppu_x, self.loppu_y = alku_x, alku_y, loppu_x, loppu_y
        self.verkko = verkko
        self.alku: Solmu = verkko.hae_solmu(alku_x, alku_y)
        self.loppu: Solmu = verkko.hae_solmu(loppu_x, loppu_y)
        self.etäisyysmatriisi = [[float("inf") for _ in range(verkko.hae_leveys()) ] for _ in range(verkko.hae_pituus())]
        self.vierailtu = [[False for _ in range(verkko.hae_leveys())] for _ in range(verkko.hae_pituus())]
        self.keko = []
        self.lyhin_reitti = []
        self.viive = 0
        if visualisoi:
            self.tarkkailija = tarkkailija
            self.viive = 0.02 # 20ms


    def aloita(self):
        """
        GUI:n rajapintaa varten
        """
        self.lyhin_polku()
        return self.get_lyhin_reitti()
        
    def lyhin_polku(self):
        """
        Laskee lyhimmän polun luokan konstruktorissa annettujen parametrien perusteella.
        Palauttaa <float> arvoisen etäisyyden, joka on lyhin polku jos tällainen polku on.
        Palauttaa -1 jos alku- ja loppusolmut ovat samat.
        Palauttaa inf jos reittiä ei ole.
        """
        if self.on_mahdoton(self.alku_x, self.alku_y, self.loppu_x, self.loppu_y):
            return -1 # Alku sama kuin loppu 
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
        return self.etäisyysmatriisi[self.loppu_x][self.loppu_y]
                    
    def get_lyhin_polku(self):
        return self.etäisyysmatriisi[self.loppu_x][self.loppu_y]

    def on_mahdoton(self, x1, y1, x2, y2):
        return x1 == x2 and y1 == y2 or self.verkko.hae_solmu(x1, y1) == 0 or self.verkko.hae_solmu(x2, y2) == 0
    
    def ei_rajojen_sisällä(self, x1, y1, x2, y2):
        max_h = self.verkko.hae_pituus() - 1
        max_w = self.verkko.hae_leveys() - 1
        return (x1 > max_h or y1 > max_w or x2 > max_h or y2 > max_w) 

    def get_lyhin_reitti(self):
        """
        Palauttaa listan tupleja (x, y) jotka muodostavat lyhimmän reitin backtrackaamalla.
        Jos alkusolmu on este, palauttaa tyhjän listan. 
        Jos polkua ei ole, palauttaa vain loppusolmun
        """
        lyhin_reitti = []
        if self.alku == 0:
            return []
        self.alku.set_edeltäjä(None)
        if len(lyhin_reitti) < 1:
            nyky = self.loppu
            lyhin_reitti.append(self.loppu.get_koordinaatit())
            while True:
                edeltäjä = nyky.get_edeltäjä()
                if edeltäjä:
                    lyhin_reitti.append(edeltäjä.get_koordinaatit())
                    nyky = edeltäjä
                else: 
                    lyhin_reitti.reverse()
                    break
        return lyhin_reitti
    
    
    


        