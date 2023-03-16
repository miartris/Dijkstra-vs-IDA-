import pytest
from datastructs import keko
import random
from math import sqrt, floor

class TestKeko:
    
    @pytest.fixture(autouse=True)
    def jono(self):
        return keko.Binäärikeko()
    
    def test_koko(self, jono):
        lisää = random.randint(10, 20)
        poista = random.randint(1,9)
        koko = lisää - poista
        for i in range(lisää):
            jono.lisää(i)
        for i in range(poista):
            jono.poista()
        assert(jono.len == koko)
        
    def test_poista_pienin(self, jono):
        väli = random.randint(1,30)
        for _ in range(0, väli):
            alkio = random.randint(1, 100)
            jono.lisää(alkio)
        pienin = jono.poista()
        assert(pienin <= min(jono.get_keko()))

    def test_poista_pienin_tuple(self, jono):
        for i in range(500, random.randint(501, 1000)):
            etäisyydet = (1, sqrt(2))
            ind = random.randint(0, 1)
            alkio = (etäisyydet[ind], i, None)      # Vertailussa ensin etäisyys, sitten järj. numero
            jono.lisää(alkio)
        pienin = jono.poista()
        assert(pienin <= min(jono.get_keko()))

    def test_poista_monta(self, jono):
        for i in range(500, random.randint(501, 1000)):
            etäisyydet = (1, sqrt(2))
            ind = random.randint(0, 1)
            alkio = (etäisyydet[ind], i, None)      # Vertailussa ensin etäisyys, sitten järj. numero
            jono.lisää(alkio)
            lista = []
        for _ in range(floor(jono.get_pituus()/2)):
            lista.append(jono.poista())
        assert(lista[-1] <= min(jono.get_keko()))
            
    def test_poista_tyhjästä(self, jono):
        assert(jono.poista() == None)


        


