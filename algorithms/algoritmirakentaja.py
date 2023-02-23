from datastructs.graph import Graph
from algorithms.dijkstra import Dijkstra 
from algorithms.idastar import IdaStar

class Algoritmirakentaja():
    def __init__(self, algoritmi, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph, visualisoi=False):
        if algoritmi == "Dijkstra":
            return Dijkstra(alku_x, alku_y, loppu_x, loppu_y, verkko, visualisoi=True)
        elif algoritmi == "IdaStar":
            return IdaStar(alku_x, alku_y, loppu_x, loppu_y, verkko, visualisoi=True)
    
            