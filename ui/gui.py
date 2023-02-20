import tkinter as tk
from tkinter import filedialog
from maps.tiedosto import Tiedostokäsittelijä
from random import randint
from algorithms.algoritmirakentaja import Algoritmirakentaja

class GUI:
    def __init__(self) -> None:

        self.ikkuna = tk.Tk()
        self.algoritmit = ["Dijkstra", "IDA*"]
        self.käsittelijä = Tiedostokäsittelijä()
        self.kartat = self.käsittelijä.get_kartat()
        #self.testit = self.käsittelijä.get_testit()
        self.karttatiedosto = None


        nappi_kontti = tk.Frame(self.ikkuna, width=600, height=120, background="gray")
        
        valitse_algo_arvo = tk.StringVar(self.ikkuna)
        valitse_algo_arvo.set("Valitse algo")
        
        valitse_algoritmi = tk.OptionMenu(nappi_kontti, valitse_algo_arvo, *self.algoritmit)

        valitse_kartta_arvo = tk.StringVar(self.ikkuna)
        valitse_kartta_arvo.set(("Valitse kartta"))
        valitse_kartta = tk.OptionMenu(nappi_kontti, valitse_kartta_arvo, *self.kartat)

        satunnainen_kartta = tk.Button(nappi_kontti, text="Satunnainen Kartta")
        satunnainen_kartta.bind('<Button-1>', self.valitse_satunnainen_kartta)

        aloita= tk.Button(nappi_kontti, text="Aloita")
        puskuri = 5
        valitse_algoritmi.grid(row = 0, column = 0, sticky="EW", padx=puskuri, pady=(10, 0))
        valitse_kartta.grid(row = 0, column = 1, sticky="EW", padx=puskuri, pady=(10, 0))
        satunnainen_kartta.grid(row = 0, column = 2, sticky="EW", padx=puskuri, pady=(10, 0))
        aloita.grid(row = 1, column = 1, sticky="EW", pady=10)

        for sarake in range(0,3):
            nappi_kontti.grid_columnconfigure(sarake, weight=1)
            for rivi in range(0,2):
                nappi_kontti.grid_rowconfigure(rivi, weight=rivi+1)

        piirtokenttä = tk.Canvas(self.ikkuna, bg="white", height=400, width=600)
        nappi_kontti.pack(fill="x")
        piirtokenttä.pack(fill="both", expand=True)
    
    def valitse_karttapolku(self, e):
        self.karttatiedosto = filedialog.askopenfilename()

    def valitse_satunnainen_kartta(self, e):
        self.karttatiedosto = self.kartat[randint(0, len(self.kartat) - 1)]



    def käynnistä(self):
        self.ikkuna.mainloop()
