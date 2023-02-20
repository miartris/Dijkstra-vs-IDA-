from algorithms.dijkstra import Dijkstra
from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori

class TestDijkstra:
    testipolku = "tests"
    tiedosto = "testmap1.txt"
    raaka = Tiedostokäsittelijä(kansiopolku=testipolku)
    matriisi = raaka.käsittele_karttatiedosto(tiedosto)
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