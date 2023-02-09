import os
from datastructs import solmu, graph

def käsittele_tiedostot(path: str):
    for tiedosto in os.listdir(path):
        with open(tiedosto, "r") as f:
            parse_to_graph(f.readlines())

def parse_to_graph(kartta: list):
    type, height, width = kartta[0], kartta[1], kartta[2]
    karttadata = kartta[4:]

    for x in range(width):
        for y in range(height):
            if sallittu(xy):
                Solmu()

def sallittu(karttapiste: str) -> True:
    sallitut = [".", "G", "S", "W"]
    return karttapiste in(sallitut)





def määritä_naapurit(xy: int, kartta: list):





