class Solmu: 
    
    # x ja y koordinaatit, naapurit sisältää kohdesolmun ja etäisyyden siihen
    def __init__(self, x: int, y: int, arvo: str) -> None:
        self.xy = (x, y)
        self.naapurit = []
        self.arvo = arvo
    
    def get_koordinaatit(self) -> (tuple):
        return (self.xy)

    def lisää_naapuri(self, naapurisolmu, etäisyys: float):
        naapuri = (naapurisolmu, etäisyys)
        self.naapurit.append(naapuri)

    def __str__(self):
        return (f"xy koordinaatit {self.xy} naapurit {self.naapurit} arvo {self.arvo}")