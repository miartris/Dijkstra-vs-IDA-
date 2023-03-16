from typing import TypeVar
from math import floor
T = TypeVar("T")

class Binäärikeko:
    """
    Minimikeko implisiittisellä taulukolla toteutetulla binääripuulla.
    Indeksointi alkaa luvusta 0. Solmun lapset ovat indekseissä k * 2 + 1 ja k * 2 + 2
    Solmun vanhempi on indeksissä floor((k - 1) / 2) 

    Käyttö:

    Funktio lisää(alkio: T), missä T on vertailtava lisää alkion säilyttäen kekorakenteen.
    poista() -> T palauttaa keon pienimmän alkion ja säilyttää kekorakenteen
    katso() -> T palauttaa pienimmän alkion, mutta ei poista sitä keosta
    """
    def __init__(self) -> None:
        self.alkiot = []  
        self.len = 0
 
    def lisää(self, alkio: T):
        """Lisää alkion minimikekoon ja korjaa kekorakenteen"""
        self.alkiot.append(alkio)
        self.len += 1
        self.siirrä_ylös(self.len - 1)

    def siirrä_ylös(self, i: int):
        """Siirtää keon loppuun lisättyä alkiota ylös keossa kunnes kekorakenne on eheä"""
        i_edeltäjä = floor((i - 1)/2)
        if self.rajojen_sisällä(i_edeltäjä) and self.alkiot[i_edeltäjä] > self.alkiot[i]:
            self.vaihda(i, i_edeltäjä)
            self.siirrä_ylös(i_edeltäjä)
        else:
            return True
        
    def siirrä_alas(self, i: int):
        """Siirtää keon juuressa olevaa alkiota alas keossa kunnes kekorakenne on eheä"""
        lapsi_o = i * 2 + 2
        lapsi_v = i * 2 + 1
        while lapsi_v < self.len:
            pienin = lapsi_v
            if self.rajojen_sisällä(lapsi_o) and self.alkiot[lapsi_o] < self.alkiot[lapsi_v]:
                pienin = lapsi_o
            if self.rajojen_sisällä(pienin) and self.alkiot[i] > self.alkiot[pienin]:
                self.vaihda(i, pienin)
                self.siirrä_alas(pienin)
            else:
                return True
            
    def poista(self) -> T: 
        """Poistaa pienimmän alkion keosta ja korjaa kekorakenteen"""
        if self.on_tyhjä():
            return None
        self.vaihda(0, self.len - 1)
        pienin = self.alkiot.pop()
        self.len -= 1
        self.siirrä_alas(0)
        return pienin

    def rajojen_sisällä(self, index: int):
        """Tarkistaa, että indeksi ei osoita listan ulkopuolelle"""
        return index >= 0 and index < len(self.alkiot)

    def vaihda(self, a: int, b: int):
        """Ottaa kaksi listaindeksiä ja vaihtaa niiden osoittamat alkiot päittäin"""
        t = self.alkiot[a]
        self.alkiot[a] = self.alkiot[b]
        self.alkiot[b] = t
        return True

    def katso(self) -> T:
        """Palauttaa viitteen keon pienimpään alkioon"""
        return self.alkiot[0]

    def on_tyhjä(self) -> bool:
        return self.len == 0
    
    def get_pituus(self) -> int:
        return self.len
    
    def get_keko(self) -> list[T]:
        """Palauttaa kekolistan"""
        return self.alkiot



    


