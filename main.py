from sys import argv
import maps.tiedosto
import maps.verkkogeneraattori
from algorithms.dijkstra import Dijkstra
from ui.gui import GUI

testipolku = "tests/testmaps/testmap1.txt"
raaka = maps.tiedosto.Tiedostokäsittelijä(testipolku)
matriisi = raaka.käsittele_karttatiedosto()
graph = maps.verkkogeneraattori.Verkkogeneraattori(matriisi)
verkko = graph.luo_verkko()
dijk = Dijkstra(44, 30, 43, 28, verkko)
print(dijk.get_lyhin_polku())

