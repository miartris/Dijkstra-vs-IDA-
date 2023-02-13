from datastructs.solmu import Solmu


# Representoi verkkoa vieruslistana

class Graph:
    
    # Luo tyhjä lista kartan mitoilla
    def __init__(self, xdim, ydim) -> None:
        self.leveys = xdim
        self.pituus = ydim
        self.solmut: list = [[0 for _ in range(xdim)] for _ in range(ydim)]
    
    # Lisää solmun verkkoon sen xy koordinaattien perusteella
    def lisaa_solmu(self, solmu: Solmu) -> None:
        xy = solmu.get_koordinaatit()
        x, y = xy
        self.solmut[x][y] = solmu
    
    def hae_solmu(self, x, y) -> Solmu:
        return self.solmut[x][y]

    def hae_solmut(self):
        return self.solmut
    
    def hae_leveys(self):
        return self.leveys
    
    def hae_pituus(self):
        return self.pituus