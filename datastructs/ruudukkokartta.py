class RuudukkoTehdas():
    """Luo tehdas, joka luo halutun kokoisia ruudukoita"""
    def __init__(self) -> None:
        """Alustaa tehtaan"""
        pass

    def luo_ruudukko(self, korkeus, leveys):
        return RuudukkoKartta(korkeus, leveys)

class RuudukkoKartta:
    """
    Luo listan merkkijonoja, jotka koostuvat merkistä '.' tai esteestä 'T'
    Representoi 2D-Ruudukkoa
    """
    def __init__(self, korkeus, leveys):
        self.leveys = leveys
        self.korkeus = korkeus
        self.ruudukko = [("." * self.leveys) for _ in range(self.korkeus)]

    def get_kartta(self):
        """
        Palauttaa merkkijonolistan
        """
        return self.ruudukko

    def luo_este(self, x, y):
        """
        Korvaa merkin '.' merkillä 'T' koordinaatissa xy
        """
        rivi_listana = list(self.ruudukko[x])
        rivi_listana[y] = "T"
        merkkijonona = "".join(rivi_listana)
        self.ruudukko[x] = merkkijonona
    
    def tuhoa_esteet(self):
        for string in self.ruudukko:
            string.replace("T", ".")

        
