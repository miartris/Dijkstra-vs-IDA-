import tkinter as tk
from tkinter import messagebox
from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori
from random import randint
from math import floor
from algorithms.algoritmirakentaja import Algoritmirakentaja
from enum import Enum
import time
from datastructs.ruudukkokartta import RuudukkoTehdas
from datastructs.tila import Tila
import concurrent.futures

class GUI:
    def __init__(self) -> None:

        self.ikkuna = tk.Tk()
        self.algoritmit = ["Dijkstra", "IdaStar"]
        self.algoritmi = None
        self.käsittelijä = Tiedostokäsittelijä()
        self.generaattori = None
        self.kartat = self.käsittelijä.get_kartat()
        #self.testit = self.käsittelijä.get_testit()
        self.karttatiedosto = None
        self.alku = ()
        self.loppu = ()
        self.korkeus = 5
        self.leveys = 5
        self.canvas_height = 800
        self.canvas_width = 800
        self.piirtokenttä = tk.Canvas(self.ikkuna, bg="white", height=self.canvas_height, width=self.canvas_width)
        self.piirtokenttä.bind("<B1-Motion>", self.hiiri_koordinaatit)
        self.piirtokenttä.bind("<Button-1>", self.hiiri_koordinaatit)
        self.ruudukkotehdas = RuudukkoTehdas()
        self.ruudukko_olio = self.ruudukkotehdas.luo_ruudukko(5,5)
        self.ruudukko = self.ruudukko_olio.get_kartta()
        self.dimensiot = [k for k in range(5, 51)]
        self.piirtotila = None
        nappi_kontti = tk.Frame(self.ikkuna, width=800, height=120, border=2)
        
        self.valitse_algo_arvo = tk.StringVar(self.ikkuna)
        self.valitse_algo_arvo.set("Valitse algo")
        
        valitse_algoritmi = tk.OptionMenu(nappi_kontti, self.valitse_algo_arvo, *self.algoritmit)

        self.valitse_kartta_arvo = tk.StringVar(self.ikkuna)
        self.valitse_kartta_arvo.set(("Valitse kartta"))
        valitse_kartta = tk.OptionMenu(nappi_kontti, self.valitse_kartta_arvo, *self.kartat)

        satunnainen_kartta = tk.Button(nappi_kontti, text="Satunnainen Kartta")
        satunnainen_kartta.bind('<Button-1>', self.valitse_satunnainen_kartta)

        valitse_korkeus_teksti = tk.Label(nappi_kontti, text="Valitse korkeus", anchor="e")
        self.valitse_korkeus = tk.IntVar(self.ikkuna)
        self.valitse_korkeus.set((5))
        valitse_korkeus = tk.OptionMenu(nappi_kontti, self.valitse_korkeus, *self.dimensiot, command=self.päivitä_ruudukko)

        valitse_leveys_teksti = tk.Label(nappi_kontti, text="Valitse leveys")
        self.valitse_leveys = tk.IntVar(self.ikkuna)
        self.valitse_leveys.set((5))
        valitse_leveys = tk.OptionMenu(nappi_kontti, self.valitse_leveys, *self.dimensiot, command=self.päivitä_ruudukko)

        tyhjennä = tk.Button(nappi_kontti, text="Tyhjennä ruudukko")
        tyhjennä.bind("<Button-1>", self.tyhjennä)

        self.radiovar = tk.IntVar(self.ikkuna)
        params = {}
        valitse_alkupiste = tk.Radiobutton(nappi_kontti, text="Valitse alkupiste", command=self.muuta_tila, variable=self.radiovar, value=1)
        valitse_loppupiste = tk.Radiobutton(nappi_kontti, text="Valitse loppupiste", command=self.muuta_tila, variable=self.radiovar, value=2)
        piirrä_esteet = tk.Radiobutton(nappi_kontti, text="Piirrä esteitä", command=self.muuta_tila, variable=self.radiovar, value=3)

        aloita = tk.Button(nappi_kontti, text="Aloita")
        aloita.bind('<Button-1>', self.suorita_algoritmi)
        
        puskuri = 5
        valitse_algoritmi.grid(row = 0, column = 0, sticky="EW", padx=puskuri, pady=(10, 0))
        #valitse_kartta.grid(row = 0, column = 2, sticky="EW", padx=puskuri, pady=(10, 0))
       # satunnainen_kartta.grid(row = 0, column = 4, sticky="EW", padx=puskuri, pady=(10, 0))
        valitse_leveys_teksti.grid(row = 2, column = 0, pady=(10, 0))
        valitse_leveys.grid(row = 3, column = 0, sticky="NSEW", pady=(0, 0))
        valitse_korkeus_teksti.grid(row = 2, column = 2)
        valitse_korkeus.grid(row = 3, column = 2, sticky="NSEW", pady=(0, 0))
        tyhjennä.grid(row=3, column=4, sticky="NSEW")
        aloita.grid(row = 5, column = 2, sticky="EW", pady=10)
        valitse_alkupiste.grid(row = 4, column = 0, sticky = "EW", pady=10, padx=puskuri)
        valitse_loppupiste.grid(row = 4, column = 2, sticky = "EW", pady=10, padx=puskuri)
        piirrä_esteet.grid(row = 4, column = 4, sticky = "EW", pady=10, padx=puskuri)

        for sarake in range(0,5):
            nappi_kontti.grid_columnconfigure(sarake, weight=1)
            for rivi in range(0,5):
                nappi_kontti.grid_rowconfigure(rivi, weight=1)

        nappi_kontti.pack(fill="x")
        self.piirtokenttä.pack(expand=True)
        self.ikkuna.title("Reitinhakusovellus")
        self.ikkuna.after(500, self.piirrä_kartta, self.ruudukko)
    
    def valitse_satunnainen_kartta(self, e):
        self.karttatiedosto = self.kartat[randint(0, len(self.kartat) - 1)]
        self.valitse_kartta_arvo.set(self.karttatiedosto)

    def suorita_algoritmi(self, e):
        if self.valitse_algo_arvo.get() == "Valitse algo":
            messagebox.showerror("No algorithm", "Valitse jokin algoritmi")
            return
        nykykartta = self.valitse_kartta_arvo.get()
        #if nykykartta != "Valitse kartta":
        #karttatiedot = self.käsittelijä.käsittele_karttatiedosto(nykykartta)
        #self.korkeus = karttatiedot["korkeus"]
        #self.leveys = karttatiedot["leveys"]
        self.korkeus = self.korkeus
        self.leveys = self.leveys
        #self.piirrä_kartta(karttatiedot["karttadata"])
        #self.piirrä_kartta(self.ruudukko)
        self.generaattori = Verkkogeneraattori({"korkeus":self.leveys, "leveys":self.korkeus, "karttadata":self.ruudukko})
        verkko = self.generaattori.luo_verkko()
        x1, y1 = self.alku
        x2, y2 = self.loppu
        self.algoritmi = Algoritmirakentaja(self.valitse_algo_arvo.get(), x1, y1, x2, y2, verkko, visualisoi=True, tarkkailija=self).rakenna_algoritmi()
        #with concurrent.futures.ThreadPoolExecutor() as ex:
            #reitti = ex.submit(self.algoritmi.aloita)
            #reitti = reitti.result()
        reitti = self.algoritmi.aloita()
        self.piirrä_polku(reitti)
        self.ikkuna.after(3000, self.palauta, self.ruudukko)

    def tyhjennä(self):
        self.piirtokenttä.delete('all')

    def muuta_tila(self):
        lähde = self.radiovar.get()
        if lähde == 1:
            self.piirtotila = Piirtotila.ALKU
        elif lähde == 2:
            self.piirtotila = Piirtotila.LOPPU
        elif lähde == 3:
            self.piirtotila = Piirtotila.ESTE

    def piirrä_kartta(self, karttadata: list):
        '''
        Värittää nelikuutioita kartasta sen mukaan onko ruutu vapaa vai este
        Tekee tarvittavat muunnokset, jotta kartan ja piirtoalustan suhde säilyy ehjänä
        '''
        h = self.korkeus
        w = self.leveys
        ch = self.piirtokenttä.winfo_height()
        cw = self.piirtokenttä.winfo_width()
        sallitut = [".", "G", "S", "W"]
        
        for i, jono in enumerate(karttadata):
            for j, kirjain in enumerate(jono):
                if kirjain in(sallitut):
                    self.piirtokenttä.create_rectangle([(j * ch/h, i * cw/w), ((j+1) * ch/h), ((i+1) * cw/w)], fill="white")
                else:
                    self.piirtokenttä.create_rectangle([(j * ch/h, i * cw/w), ((j+1) * ch/h), ((i+1) * cw/w)], fill="black")

    def palauta(self, karttadata):
        self.alku = ()
        self.loppu = ()
        self.ruudukko_olio.tuhoa_esteet()
        self.ruudukko = self.ruudukko_olio.get_kartta()
        print(self.ruudukko)
        self.piirrä_kartta(self.ruudukko)
   
    def hiiri_koordinaatit(self, event):
        x = event.x
        y = event.y
        mx, my = self.muunna_koordinaatit((x,y))
        self.päivitä_solmu(mx, my)
        return (x,y)

    def päivitä_ruudukko(self, event):
        self.tyhjennä()
        h = self.valitse_korkeus.get()
        w = self.valitse_leveys.get()
        self.korkeus, self.leveys = w, h
        self.ruudukko_olio = self.ruudukkotehdas.luo_ruudukko(h, w)
        self.ruudukko = self.ruudukko_olio.get_kartta()
        self.piirrä_kartta(self.ruudukko)

    def muunna_koordinaatit(self, xy):
        x, y = xy
        kartta_x = floor(x / (self.piirtokenttä.winfo_height()/self.korkeus))
        kartta_y = floor(y / (self.piirtokenttä.winfo_width()/self.leveys))
        return (kartta_x, kartta_y)

    def päivitä_solmu(self, x, y):
        if not self.piirtotila:
            messagebox.showerror(message="Valitse jokin piirtotila")
            return
        h = self.korkeus
        w = self.leveys
        ch = self.piirtokenttä.winfo_height()
        cw = self.piirtokenttä.winfo_width()
        self.piirtokenttä.create_rectangle([(x * ch/h, y * cw/w), ((x+1) * ch/h), ((y+1) * cw/w)], fill=self.piirtotila.value)
        self.päivitä_alkutila((y, x))

    def piirrä_polku(self, polku: list):
       # prev_state = self.piirtotila.name
        self.piirtotila = Piirtotila.POLKU
        polku = polku[1:-1]        
        for solmu in polku:
            self.päivitä_solmu(solmu[1], solmu[0])
        #self.piirtotila = prev_state
    
    def päivitä_alkutila(self, xy):
        if self.piirtotila == Piirtotila.ALKU:
            self.alku = xy
        elif self.piirtotila == Piirtotila.LOPPU:
            self.loppu = xy
        elif self.piirtotila == Piirtotila.ESTE:
            y, x = xy
            self.ruudukko_olio.luo_este(y, x)
            self.ruudukko = self.ruudukko_olio.get_kartta()

    def päivitä_tila(self, solmu: tuple, tila: Tila, vakiot: list, viive):
        """
        Saa solmu. Päivitä ruudukko saadun solmun tilan perusteella.
        Luovuttaa prioriteetin suorittavalla säikeelle
        """
        y, x = solmu
        self.piirtotila = tila
        if solmu not in vakiot: # Solmu ei loppu tai alku
            self.päivitä_solmu(x, y)
        self.ikkuna.update()
        time.sleep(viive)

    def käynnistä(self):
          self.ikkuna.mainloop()

class Piirtotila(Enum):
    ALKU = "green"
    LOPPU = "red"
    ESTE = "black"
    POLKU = "blue"