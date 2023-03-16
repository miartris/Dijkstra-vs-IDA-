from algorithms.idastar import IdaStar
from algorithms.dijkstra import Dijkstra
from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori
import pytest

class TestIda_Star:
    testipolku = "tests"
    tiedosto = "testmap3.txt"
    testitiedosto = "testscen3.txt"
    raaka = Tiedostokäsittelijä(kansiopolku=testipolku)
    matriisi = raaka.käsittele_karttatiedosto(tiedosto)
    testit = raaka.parse_testi("testscen3.txt")
    graph = Verkkogeneraattori(matriisi)
    verkko = graph.luo_verkko()

    def test_heuristiikka(self):
        pass

    def test_polku_itseensä(self):
        ida = IdaStar(29, 8, 29, 8, self.verkko).runko()
        tulos = round(ida["etäisyys"], 8)
        assert (tulos == float("inf"))

    def test_ei_polkua(self):
        ida = IdaStar(0, 0, 0, 1, self.verkko).runko()
        tulos = round(ida["etäisyys"], 8)
        assert (tulos == float("inf"))

    def test_oikeat_etäisyydet(self):
        testit = self.testit[:50]
        for index, t in enumerate(testit):
            ida = IdaStar(t["y1"], t["x1"], t["y2"], t["x2"], self.verkko).runko() 
            polku = round(ida["etäisyys"], 5)
            etäisyys = round(Dijkstra(t["y1"], t["x1"], t["y2"], t["x2"], self.verkko).lyhin_polku(), 5)
            assert(polku == etäisyys)