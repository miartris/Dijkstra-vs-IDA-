from abc import ABC, abstractmethod

class Algoritmi(ABC):

    @abstractmethod
    def aloita(self):
        pass

    def on_mahdoton(self):
        pass