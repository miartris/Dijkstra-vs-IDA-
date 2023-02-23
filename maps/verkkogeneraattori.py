from datastructs.graph import Graph
from datastructs.solmu import Solmu
from math import sqrt

# Luo verkkorakenteen käyttäen pohjana 2D-Ruudukkomaista karttadataa. Matriisiparametri on {"leveys:<leveys>, korkeus:<korkeus>, karttadata:<karttadata>"}
class Verkkogeneraattori:

    def __init__(self, matriisi) -> None:
        self.karttadata = matriisi["karttadata"]
        self.height = matriisi["korkeus"]
        self.width = matriisi["leveys"]
        self.verkko = Graph(self.height, self.width)

    def luo_verkko(self) -> Graph:
        for x in range(self.height):
            for y in range(self.width):
                karttapiste = self.karttadata[x][y]
                if self.sallittu(karttapiste):
                    uusi_solmu = Solmu(x, y, karttapiste)
                    self.verkko.lisaa_solmu(uusi_solmu)
        for list in self.verkko.hae_solmut():
            for solmu in list:
                if solmu != 0:
                    self.määritä_naapurit(solmu, self.karttadata, self.verkko)

        return self.verkko

    def sallittu(self, karttapiste: str) -> bool:
        sallitut = [".", "G", "S", "W"]
        return karttapiste in(sallitut)

   
    def määritä_naapurit(self, solmu: Solmu, kartta: list, verkko: Graph):
        """
        Määrittää jokaisen solmun kaaret sen vierussolmuihin. 
        Jos diagonaalinen polku menee esteiden vierestä tai lävitse, se kierretään
        """
        max_h = len(kartta) - 1
        max_w = len(kartta[0]) - 1
        solmu_x, solmu_y = solmu.get_koordinaatit()
        
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not(dx == 0 and dy == 0):
                    naapuri_x = solmu_x + dx
                    naapuri_y = solmu_y + dy
                    if self.rajojen_sisällä(max_h, max_w, naapuri_x, naapuri_y):
                        if self.sallittu(kartta[naapuri_x][naapuri_y]):
                            on_diagonaalinen = self.on_diagonaalinen(dx, dy)
                            # Lisää diagonaalinen naapuri vain, jos diagonaalisella polulla ei mennä seinän läpi
                            if on_diagonaalinen and not self.diagonaalinen_liike_sallittu(kartta, solmu_x, solmu_y, dx, dy):
                                continue
                            etäisyys = 1 if not on_diagonaalinen else sqrt(2)
                            naapuri = verkko.hae_solmu(naapuri_x, naapuri_y)
                            solmu.lisää_naapuri(naapuri, etäisyys)
                        
    def rajojen_sisällä(self, max_korkeus, max_leveys, x, y):
        return not(x < 0 or x > max_korkeus or y < 0 or y > max_leveys)

    def on_diagonaalinen(self, dx, dy):
        arvot = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
        return((dx, dy) in arvot)
    
    # Tarkista, ovatko molemmat ruudut joiden välistä liikutaan vapaita
    def diagonaalinen_liike_sallittu(self, kartta, x, y, dx, dy):
        # Vasemmalle ylös
        if (dx, dy) == (-1, -1):
            return self.sallittu(kartta[x][y-1]) and self.sallittu(kartta[x-1][y])
        # Oikealle ylös
        elif (dx, dy) == (-1, 1): 
            return self.sallittu(kartta[x][y+1]) and self.sallittu(kartta[x-1][y])
        # Vasemmalle alas
        elif (dx, dy) == (1, -1):
            return self.sallittu(kartta[x][y-1]) and self.sallittu(kartta[x+1][y])
        # Oikealle alas
        elif (dx, dy) == (1, 1):
            return self.sallittu(kartta[x][y+1]) and self.sallittu(kartta[x+1][y])