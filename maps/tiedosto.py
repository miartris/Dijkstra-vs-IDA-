import os
from datastructs.solmu import Solmu
from datastructs.graph import Graph
from re import findall
from math import sqrt

def käsittele_tiedostot(polku: str):
    for tiedosto in os.listdir(polku):
        tiedosto_polku = os.path.join(polku, tiedosto)
        with open(tiedosto_polku, "r") as f:
            parse_to_graph(f.readlines())

def parse_to_graph(kartta: list):
    # Korkeus indeksissä 1 leveys indeksissä 2
    height, width = [int (val) for val in findall(r'\d+', kartta[1] + kartta[2])]
    verkko = Graph(width, height)
    # Älä sisällytä viimeistä tyhjää riviä
    karttadata = kartta[4:len(kartta)]

    for x in range(width):
        for y in range(height):
            karttapiste = karttadata[x][y]
            if sallittu(karttapiste):
                uusi_solmu = Solmu(x, y, karttapiste)
                verkko.lisaa_solmu(uusi_solmu)
                print(f" solmu {uusi_solmu}")
    for list in verkko.hae_solmut():
        for solmu in list:
            if solmu != 0:
                määritä_naapurit(solmu, karttadata, verkko)

    return verkko

def sallittu(karttapiste: str) -> True:
    sallitut = [".", "G", "S", "W"]
    return karttapiste in(sallitut)

def määritä_naapurit(solmu: Solmu, kartta: list, verkko: Graph):
    max_h = len(kartta) - 1
    max_w = len(kartta[0]) - 1
    solmu_x, solmu_y = solmu.get_koordinaatit()
    
    for dx in range(-1, 1):
        for dy in range(-1, 1):
            if not(dx == 0 and dy == 0):
                naapuri_x = solmu_x + dx
                naapuri_y = solmu_y + dy
                if sallittu(kartta[naapuri_x][naapuri_y]) and rajojen_sisällä(max_h, max_w, naapuri_x, naapuri_y):
                    etäisyys = 1 if not on_diagonaalinen(dx, dy) else sqrt(2)
                    naapuri = verkko.hae_solmu(naapuri_x, naapuri_y)
                    solmu.lisää_naapuri(naapuri, etäisyys)
                    
def rajojen_sisällä(max_korkeus, max_leveys, x, y):
    return not(x < 0 or x > max_leveys or y < 0 or y > max_korkeus)

def on_diagonaalinen(dx, dy):
    arvot = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    return((dx, dy) in arvot)










