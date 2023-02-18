from datastructs.graph import Graph
from datastructs.solmu import Solmu
from math import sqrt

class Verkkogeneraattori:
    
    def __init__(self, matriisi) -> None:
        self.karttadata = matriisi["karttadata"]
        self.width = matriisi["leveys"]
        self.height = matriisi["korkeus"]
        self.verkko = Graph(self.width, self.height)

    def luo_verkko(self) -> Graph:
        for x in range(self.width):
            for y in range(self.height):
                karttapiste = self.karttadata[x][y]
                if self.sallittu(karttapiste):
                    uusi_solmu = Solmu(x, y, karttapiste)
                    self.verkko.lisaa_solmu(uusi_solmu)
        for list in self.verkko.hae_solmut():
            for solmu in list:
                if solmu != 0:
                    self.määritä_naapurit(solmu, self.karttadata, self.verkko)

        return self.verkko

    def sallittu(self, karttapiste: str) -> True:
        sallitut = [".", "G", "S", "W"]
        return karttapiste in(sallitut)

    def määritä_naapurit(self, solmu: Solmu, kartta: list, verkko: Graph):
        max_h = len(kartta) - 1
        max_w = len(kartta[0]) - 1
        solmu_x, solmu_y = solmu.get_koordinaatit()
        
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not(dx == 0 and dy == 0):
                    naapuri_x = solmu_x + dx
                    naapuri_y = solmu_y + dy
                    if self.sallittu(kartta[naapuri_x][naapuri_y]) and self.rajojen_sisällä(max_h, max_w, naapuri_x, naapuri_y):
                        etäisyys = 1 if not self.on_diagonaalinen(dx, dy) else sqrt(2)
                        naapuri = verkko.hae_solmu(naapuri_x, naapuri_y)
                        solmu.lisää_naapuri(naapuri, etäisyys)
                        
    def rajojen_sisällä(self, max_korkeus, max_leveys, x, y):
        return not(x < 0 or x > max_leveys or y < 0 or y > max_korkeus)

    def on_diagonaalinen(self, dx, dy):
        arvot = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
        return((dx, dy) in arvot)