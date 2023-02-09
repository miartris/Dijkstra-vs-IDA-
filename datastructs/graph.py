from solmu import Solmu

# Representoi verkkoa vieruslistana
# Dictissä avain on pisteen (x, y) koordinaatti arvo on sen naapurit
class Graph:
    
    def __init__(self) -> None:
        self.solmut: list = {}

    def lisaa_solmu(self, solmu: Solmu) -> None:
        self.solmut.append(solmu)
