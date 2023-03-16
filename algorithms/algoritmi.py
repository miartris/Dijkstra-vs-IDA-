from abc import ABC, abstractmethod

class Algoritmi(ABC):
    """
    Pohja algoritmeille. Määrittää geneeristä toiminnallisuutta
    """

    @abstractmethod
    def aloita(self):
        pass

    def on_mahdoton(self):
        pass

    def keskeytä(self):
        pass