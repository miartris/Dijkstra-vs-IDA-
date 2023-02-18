from algorithms.dijkstra import Dijkstra
from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori



class TestDijkstra:
    testipolku = "tests/testmaps/testmap1.txt"
    raaka = Tiedostokäsittelijä(testipolku)
    matriisi = raaka.käsittele_karttatiedosto()
    graph = Verkkogeneraattori(matriisi)
    verkko = graph.luo_verkko()

    def test_yksinkertainen(self):
        dijk = Dijkstra(28, 14, 5, 32, self.verkko)
        tulos = round(dijk.get_lyhin_polku(), 8)
        assert (tulos == 30.45584412)

    def test_lyhin_reitti(self):
        dijk = Dijkstra(19, 26, 19, 29, self.verkko)
        tulos = dijk.get_lyhin_reitti()
        assert(tulos == [(19, 26), (19, 27), (19, 28), (19, 29)])