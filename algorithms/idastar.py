from datastructs.solmu import Solmu
from datastructs.graph import Graph
from math import sqrt

class IdaStar:
    def __init__(self, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph, visualisoi=False, init_olio=None):
        self.alku_x, self.alku_y, self.loppu_x, self.loppu_y = alku_x, alku_y, loppu_x, loppu_y
        self.verkko = verkko
        self.alku: Solmu = verkko.hae_solmu(alku_x, alku_y)
        self.loppu: Solmu = verkko.hae_solmu(loppu_x, loppu_y)

    """
    Karsivana etäisyytenä käytetään oktiilietäisyyttä (octile distance)
    Soveltuu lukuisista etäisyysarvioista parhaiten tilanteeseen, jossa voidaan liikkua diagonaalisesti
    """
    def heuristiikka(self, solmu):
        x, y = solmu.get_koordinaatit()
        dx = (abs(x - self.loppu_x))
        dy = (abs(y - self.loppu_y))
        # Ortogonaalinen etäisyys on 1, diagonaalinen sqrt(2)
        etäisyysarvio = (1 * (dx + dy) + (sqrt(2) - 2) * min(dx, dy))
        return etäisyysarvio

