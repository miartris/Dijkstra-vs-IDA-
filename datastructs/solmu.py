from datastructs.tila import Tila

class Solmu: 
    """
    Verkon solmun representaatio.
    Arvot: xy-koordinaattipari, lista naapurisolmusta ja etäisyydestä, str-arvo kuten '.' tai 'T',
    edeltäjäsolmu, jolla dijkstran algoritmissa määritetään lyhin polku backtrackaamalla
    """
    
    def __init__(self, x: int, y: int, arvo: str) -> None:
        self.xy = (x, y)
        self.naapurit = []
        self.arvo = arvo
        self.edeltäjä = None
        self.tila = None
    
    def get_koordinaatit(self) -> (tuple):
        return (self.xy)

    def lisää_naapuri(self, naapurisolmu, etäisyys: float):
        naapuri = (naapurisolmu, etäisyys)
        self.naapurit.append(naapuri)
    
    def get_naapurit(self):
        """
        Palauttaa listan naapureista ja etäisyydestä niihin. Tupleja (<Solmu>, <float>)
        """
        return self.naapurit

    def __str__(self):
        return (f"xy koordinaatit {self.xy} naapurit {self.naapurit} arvo {self.arvo}")

    def get_tila(self):
        return self.tila

    def set_edeltäjä(self, solmu):
        self.edeltäjä = solmu
    
    def get_edeltäjä(self):
        return self.edeltäjä

    def muuta_tila(self, uusi_tila):
        self.tila = uusi_tila