class RuudukkoKartta:
    def __init__(self, korkeus, leveys):
        self.korkeus = korkeus
        self.leveys = leveys
        self.ruudukko = []

    def rakenna_kartta(self):
        self.ruudukko = [("." * self.leveys) for _ in range(self.korkeus)]
        return self.ruudukko

    def luo_este(self, x, y):
        self.ruudukko[x][y] = "T"
        
