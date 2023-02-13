from datastructs.solmu import Solmu 
from datastructs.graph import Graph
from maps import tiedosto
from algorithms.dijkstra import Dijkstra

testipolku = "tests/testmaps/testmap1.txt"
graph = tiedosto.käsittele_tiedosto(testipolku)
polut = Dijkstra(19, 26, 19, 29, graph)
lyhimmät = polut.get_lyhin_polku()
print(lyhimmät)


