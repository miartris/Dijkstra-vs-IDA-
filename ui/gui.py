import tkinter as tk

class GUI:
    def __init__(self, algoritmit=None) -> None:

        ikkuna = tk.Tk()

        nappi_kontti = tk.Frame(ikkuna, width=600, height=120, background="gray")
        valitse_algoritmi = tk.Button(nappi_kontti, text="Valitse algoritmi")
        valitse_kartta = tk.Button(nappi_kontti,text="Valitse kartta")
        satunnainen_kartta = tk.Button(nappi_kontti, text="Satunnainen Kartta")
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
        
        

        

        piirtokenttä = tk.Canvas(ikkuna, bg="black", height=400, width=600)
        nappi_kontti.pack(fill="x")
        piirtokenttä.pack(fill="both", expand=True)
        ikkuna.mainloop()