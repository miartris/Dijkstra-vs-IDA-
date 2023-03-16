from maps.tiedosto import Tiedostokäsittelijä
from maps.verkkogeneraattori import Verkkogeneraattori
from time import perf_counter_ns
from datetime import datetime
from algorithms.dijkstra import Dijkstra
from algorithms.idastar import IdaStar
from functools import wraps
import csv

class Suorituskykytestaus():
    def __init__(self) -> None:
        self.kartat = "./maps"
        self.testit = "./scens"
        self.käsittelijä = Tiedostokäsittelijä(kansiopolku="./tests")
        self.kartat = self.käsittelijä.get_kartat()
        self.testit = self.käsittelijä.get_testit()
        self.lista = []
        self.ajat = {}
        for i, (kartat, testit) in enumerate(zip(self.kartat, self.testit)):
            i = (self.käsittelijä.käsittele_karttatiedosto(kartat), self.käsittelijä.parse_testi(testit))
            self.lista.append(i)

    # def ajasta(func):
    #     @wraps(func)
    #     def ajastimen_kanssa(*args, **kwargs):
    #             start = perf_counter_ns()
    #             res = func(*args, **kwargs)
    #             end = perf_counter_ns()
    #             time = end - start
    #             print(time)
    #             return res
    #     return ajastimen_kanssa

    # @ajasta        
    def dijkstra(self):
        for i in self.lista:
            kartta = Verkkogeneraattori(i[0]).luo_verkko()
            for ind, j in enumerate(i[1]):
                x = self.pura("Dijkstra", kartta, j)
                start = perf_counter_ns()
                p = x.lyhin_polku()
                end = perf_counter_ns()
                time = end - start
                self.ajat[f"{ind} dijkstra {j['kartta']}"] = (f"t: {time}", f"etäisyys {p}")
        print(self.ajat)

    def idastar(self):
        for i in self.lista:
            kartta = Verkkogeneraattori(i[0]).luo_verkko()
            for ind, j in enumerate(i[1][:40]):
                x = self.pura("Ida*", kartta, j)
                start = perf_counter_ns()
                p = x.runko()["etäisyys"]
                end = perf_counter_ns()
                time = end - start
                self.ajat[f"{ind} ida* {j['kartta']}"] = (f"t: {time}", f"etäisyys {p}")
        print(self.ajat)
        
    def pura(self, algoritmi, kartta, testi):
        if algoritmi == "Dijkstra":
            return Dijkstra(testi["y1"], testi["x1"], testi["y2"], testi["x2"], kartta)
        elif algoritmi == "Ida*":
            return IdaStar(testi["y1"], testi["x1"], testi["y2"], testi["x2"], kartta)
    
    def testaa(self):
        self.dijkstra()
        self.idastar()
        nimi = datetime.now().strftime("%Y%m%d-%H%M%S")
        with open(f"./tests/benchmark_{nimi}" + ".csv", 'a+') as f:
            writer = csv.writer(f)
            for k, v in self.ajat.items():
                writer.writerow([k, v])


    




    



        