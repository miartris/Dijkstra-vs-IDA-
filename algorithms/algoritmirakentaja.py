from datastructs.graph import Graph
from algorithms.dijkstra import Dijkstra 
from algorithms.idastar import IdaStar

class Algoritmirakentaja():
    """
    Rakentaa halutunlaisen Algoritmi-luokan toiminnallisuuden
    toteuttavan algoritmin alkuparametrien pohjalta.
    """
    def __init__(self, algoritmi, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph, visualisoi=True, tarkkailija=None):
        """
        Alustaa algoritmirakentajan. 
        Algoritmi on merkkijono, joka kertoo minkä algoritmin palauttaa. xy-parametrit ovat alku-ja maalisolmun int-koordinaatit.
        <Graph> verkko sisältää kartan, jolla algoritmi toteutetaan.
        """
        self.algoritmi = algoritmi
        self.x1, self.y1, self.x2, self.y2 = alku_x, alku_y, loppu_x, loppu_y
        self.verkko = verkko
        self.tarkkailija = tarkkailija
    
    def rakenna_algoritmi(self):
        """Palauttaa algoritmin init-parametrien perusteella"""
        if self.algoritmi == ("Dijkstra"):
            return Dijkstra(self.x1, self.y1, self.x2, self.y2, self.verkko, visualisoi=True, tarkkailija=self.tarkkailija)
        elif self.algoritmi == ("IdaStar"):
            return IdaStar(self.x1, self.y1, self.x2, self.y2, self.verkko, visualisoi=True, tarkkailija=self.tarkkailija)