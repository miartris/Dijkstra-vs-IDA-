from algorithms.dijkstra import Dijkstra
from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori
import pytest


class TestDijkstra:
    testipolku = "tests"
    tiedosto = "testmap1.txt"
    testitiedosto = "testscen1.txt"
    raaka = Tiedostokäsittelijä(kansiopolku=testipolku)
    matriisi = raaka.käsittele_karttatiedosto(tiedosto)
    testit = raaka.parse_testi("testscen1.txt")
    graph = Verkkogeneraattori(matriisi)
    verkko = graph.luo_verkko()

    def test_yksinkertainen(self):
        dijk = Dijkstra(28, 14, 5, 32, self.verkko).lyhin_polku()
        tulos = round(dijk, 8)
        assert (tulos == 30.45584412)

    def test_lyhin_reitti(self):
        dijk = Dijkstra(19, 26, 19, 29, self.verkko)
        dijk.lyhin_polku()
        tulos = dijk.get_lyhin_reitti()
        assert(tulos == [(19, 26), (19, 27), (19, 28), (19, 29)])

    def test_alku_ja_loppu_sama(self):
        dijk = Dijkstra(0, 0, 0, 0, self.verkko)
        polku = dijk.lyhin_polku()
        reitti = dijk.get_lyhin_reitti()
        assert(polku == -1 and reitti == [])

    def test_ei_reittiä(self):
        dijk = Dijkstra(0,0,20,20, self.verkko).lyhin_polku()
        assert (dijk == -1)
    
    def test_ei_rajojen_sisällä(self):
        with pytest.raises(IndexError):
            dijk = Dijkstra(0, 0, 50, 50, self.verkko).lyhin_polku()
    
    def test_oikeat_etäisyydet(self):
        testit = self.testit
        for index, t in enumerate(testit):
            dijk = Dijkstra(t["y1"], t["x1"], t["y2"], t["x2"], self.verkko) # Testikoordinaatit olettavat, että x-akseli on leveys ja y korkeus
            polku = dijk.lyhin_polku()
            print(t)
            polku = round(polku, 5)
            etäisyys = round(t["etäisyys"], 5)
            assert(polku == etäisyys)
            