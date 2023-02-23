from datastructs.graph import Graph
from algorithms.algoritmi import Algoritmi
from algorithms.dijkstra import Dijkstra 
from algorithms.idastar import IdaStar

class Algoritmirakentaja():
    def __init__(self, algoritmi, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph):
        self.algoritmi = algoritmi
        self.x1, self.y1, self.x2, self.y2 = alku_x, alku_y, loppu_x, loppu_y
        self.verkko = verkko
    
    def rakenna_algoritmi(self):
        if self.algoritmi == ("Dijkstra"):
            return Dijkstra(self.x1, self.y1, self.x2, self.y2, self.verkko, visualisoi=True)
        elif self.algoritmi == ("IdaStar"):
            return IdaStar(self.x1, self.y1, self.x2, self.y2, self.verkko, visualisoi=True)