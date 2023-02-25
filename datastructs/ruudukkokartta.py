class RuudukkoTehdas():
    def __init__(self) -> None:
        pass

    def luo_ruudukko(self, korkeus, leveys):
        return RuudukkoKartta(korkeus, leveys)

class RuudukkoKartta:
    def __init__(self, korkeus, leveys):
        self.leveys = leveys
        self.korkeus = korkeus
        self.ruudukko = [("." * self.leveys) for _ in range(self.korkeus)]

    def get_kartta(self):
        return self.ruudukko

    def luo_este(self, x, y):
        rivi_listana = list(self.ruudukko[x])
        rivi_listana[y] = "T"
        merkkijonona = "".join(rivi_listana)
        self.ruudukko[x] = merkkijonona
        print(self.ruudukko)

        
