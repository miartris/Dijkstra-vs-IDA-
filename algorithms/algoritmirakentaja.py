from abc import ABC, abstractmethod
from datastructs.graph import Graph
from datastructs.solmu import Solmu

class Algoritmi(ABC):

    @abstractmethod
    def aloita(self):
        pass

class Algoritmirakentaja():
    def __init__(self, alku_x, alku_y, loppu_x, loppu_y, verkko: Graph, visualisoi=False, *params) -> Algoritmi:
        pass
    
