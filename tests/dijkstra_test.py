from algorithms.dijkstra import Dijkstra
from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori
import pytest


class TestDijkstra:
    testipolku = "tests"
    tiedosto = "testmap3.txt"
    testitiedosto = "testscen3.txt"
    raaka = Tiedostokäsittelijä(kansiopolku=testipolku)
    matriisi = raaka.käsittele_karttatiedosto(tiedosto)
    testit = raaka.parse_testi("testscen3.txt")
    graph = Verkkogeneraattori(matriisi)
    verkko = graph.luo_verkko()

    def test_alku_ja_loppu_sama(self):
        dijk = Dijkstra(0, 0, 0, 0, self.verkko)
        polku = dijk.lyhin_polku()
        reitti = dijk.get_lyhin_reitti()
        assert(polku == -1 and reitti == [])

    def test_ei_reittiä(self):
        dijk = Dijkstra(0,0,20,20, self.verkko).lyhin_polku()
        assert (dijk == -1)
    
    def test_ei_rajojen_sisällä(self):
            dijk = Dijkstra(-1, -1, -1, -1, self.verkko).lyhin_polku()
            assert(dijk == -1)
    
    def test_oikeat_etäisyydet(self):
        testit = self.testit
        for index, t in enumerate(testit):
            dijk = Dijkstra(t["y1"], t["x1"], t["y2"], t["x2"], self.verkko) # Testikoordinaatit olettavat, että x-akseli on leveys ja y korkeus
            polku = dijk.lyhin_polku()
            polku = round(polku, 5)
            etäisyys = round(t["etäisyys"], 5)
            assert(polku == etäisyys)
            