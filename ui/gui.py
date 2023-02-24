import tkinter as tk
from tkinter import messagebox
from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori
from random import randint
from math import floor
from algorithms.algoritmirakentaja import Algoritmirakentaja


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
        self.map_height = None
        self.map_width = None
        self.canvas_height = 800
        self.canvas_width = 800
        self.piirtokenttä = tk.Canvas(self.ikkuna, bg="white", height=self.canvas_height, width=self.canvas_width)
        self.piirtokenttä.bind("<Button-1>", self.hiiri_koordinaatit)


        nappi_kontti = tk.Frame(self.ikkuna, width=600, height=120, background="gray")
        
        self.valitse_algo_arvo = tk.StringVar(self.ikkuna)
        self.valitse_algo_arvo.set("Valitse algo")
        
        valitse_algoritmi = tk.OptionMenu(nappi_kontti, self.valitse_algo_arvo, *self.algoritmit)

        self.valitse_kartta_arvo = tk.StringVar(self.ikkuna)
        self.valitse_kartta_arvo.set(("Valitse kartta"))
        valitse_kartta = tk.OptionMenu(nappi_kontti, self.valitse_kartta_arvo, *self.kartat)

        satunnainen_kartta = tk.Button(nappi_kontti, text="Satunnainen Kartta")
        satunnainen_kartta.bind('<Button-1>', self.valitse_satunnainen_kartta)

        aloita= tk.Button(nappi_kontti, text="Aloita")
        aloita.bind('<Button-1>', self.suorita_algoritmi)
        
        puskuri = 5
        valitse_algoritmi.grid(row = 0, column = 0, sticky="EW", padx=puskuri, pady=(10, 0))
        valitse_kartta.grid(row = 0, column = 1, sticky="EW", padx=puskuri, pady=(10, 0))
        satunnainen_kartta.grid(row = 0, column = 2, sticky="EW", padx=puskuri, pady=(10, 0))
        aloita.grid(row = 1, column = 1, sticky="EW", pady=10)

        for sarake in range(0,3):
            nappi_kontti.grid_columnconfigure(sarake, weight=1)
            for rivi in range(0,2):
                nappi_kontti.grid_rowconfigure(rivi, weight=rivi+1)

        nappi_kontti.pack(fill="x")
        self.piirtokenttä.pack(expand=True)
        self.ikkuna.title("Reitinhakusovellus")
    
    def valitse_satunnainen_kartta(self, e):
        self.karttatiedosto = self.kartat[randint(0, len(self.kartat) - 1)]
        self.valitse_kartta_arvo.set(self.karttatiedosto)

    def suorita_algoritmi(self, e):
        if self.valitse_algo_arvo.get() == "Valitse algoritmi":
            messagebox.showerror("No algorithm", "Select an algorithm")
            return

        self.tyhjennä()
        nykykartta = self.valitse_kartta_arvo.get()
        if nykykartta != "Valitse kartta":
            karttatiedot = self.käsittelijä.käsittele_karttatiedosto(nykykartta)
            self.map_height = karttatiedot["korkeus"]
            self.map_width = karttatiedot["leveys"]
            #self.piirrä_ruudukko()
            self.piirrä_kartta(karttatiedot["karttadata"])
            self.generaattori = Verkkogeneraattori(karttatiedot)
            verkko = self.generaattori.luo_verkko()
            x1, y1, x2, y2 = 19, 26, 19, 29
            self.päivitä_solmu(x1, y1, 'red')
            self.päivitä_solmu(x2, y2, 'blue')
            self.algoritmi = Algoritmirakentaja(self.valitse_algo_arvo.get(), x1, y1, x2, y2, verkko).rakenna_algoritmi()
            self.algoritmi.aloita()


    def tyhjennä(self):
        self.piirtokenttä.delete('all')

    def piirrä_kartta(self, karttadata: list):
        '''
        Värittää nelikuutioita kartasta sen mukaan onko ruutu vapaa vai este
        Tekee tarvittavat muunnokset, jotta kartan ja piirtoalustan suhde säilyy ehjänä
        '''
        h = self.map_height
        w = self.map_width
        ch = self.piirtokenttä.winfo_height()
        cw = self.piirtokenttä.winfo_width()
        sallitut = [".", "G", "S", "W"]
        
        for i, jono in enumerate(karttadata):
            for j, kirjain in enumerate(jono):
                if kirjain in(sallitut):
                    self.piirtokenttä.create_rectangle([(j * ch/h, i * cw/w), ((j+1) * ch/h), ((i+1) * cw/w)], fill="green")
    def hiiri_koordinaatit(self, event):
        x = event.x
        y = event.y
        print(x,y)
        self.muunna_koordinaatit((x,y))
        return (x,y)
    
    def muunna_koordinaatit(self, xy):
        x, y = xy
        kartta_x = floor(x / (self.piirtokenttä.winfo_height()/self.map_height))
        kartta_y = floor(y / (self.piirtokenttä.winfo_width()/self.map_width))
        print(kartta_y, kartta_x)


    def päivitä_solmu(self, x, y, väri):
        h = self.map_height
        w = self.map_width
        ch = self.piirtokenttä.winfo_height()
        cw = self.piirtokenttä.winfo_width()
        self.piirtokenttä.create_rectangle([(x * ch/h, y * cw/w), ((x+1) * ch/h), ((y+1) * cw/w)], fill=väri)



    def käynnistä(self):
        self.ikkuna.mainloop()



