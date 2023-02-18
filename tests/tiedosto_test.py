import pytest
from maps.tiedosto import Tiedostokäsittelijä

class TestTiedostokäsittelijä:
    tiedostopolku = "tests/testmaps/testmap1.txt"
    kansiopolku = "tests/testmaps/"
    testipolku = "tests/testscens/testscen1.txt"

    @pytest.fixture
    def luo_käsittelijä(self):
        return Tiedostokäsittelijä(self.tiedostopolku, self.kansiopolku, self.testipolku)
    
    def test_käsittele_tiedosto_dims(self, luo_käsittelijä):
        käsittelijä = luo_käsittelijä
        tulos = käsittelijä.käsittele_karttatiedosto()
        assert (tulos["korkeus"], tulos["leveys"]) == (49, 49)
        
    def test_karttadata(self, luo_käsittelijä):
        tulos = luo_käsittelijä.käsittele_karttatiedosto()
        assert (tulos["korkeus"], tulos["leveys"]) == (len(tulos["karttadata"][0]), len(tulos["karttadata"]))
    
    def test_testidata(self, luo_käsittelijä):
        tulos = luo_käsittelijä.parse_testi()
        haluttu = {"kartta":"arena.map", "w":49, "h":49, "x1":19, "y1":26, "x2":19, "y2":29, "etäisyys":3.00000000}
        assert tulos[0] == haluttu

    def test_testidata_käsittelee_kaikki_rivit(self, luo_käsittelijä):
        tulos = len(luo_käsittelijä.parse_testi())
        assert tulos == 130
