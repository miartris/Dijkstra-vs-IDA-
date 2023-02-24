import pytest
from maps.tiedosto import Tiedostokäsittelijä

class TestTiedostokäsittelijä:

    @pytest.fixture
    def luo_käsittelijä(self):
        return Tiedostokäsittelijä(kansiopolku="tests")
    
    @pytest.fixture
    def testitiedosto(self):
        return ["testmap1.txt", "testmap2.txt"]
    
    @pytest.fixture
    def testiscen(self):
      return "testscen1.txt"
    
    def test_käsittele_tiedosto_dims(self, luo_käsittelijä, testitiedosto):
        käsittelijä = luo_käsittelijä
        tulos = käsittelijä.käsittele_karttatiedosto(testitiedosto[0])
        assert (tulos["korkeus"], tulos["leveys"]) == (49, 49)
        
    def test_karttadata(self, luo_käsittelijä, testitiedosto):
        tulos = luo_käsittelijä.käsittele_karttatiedosto(testitiedosto[0])
        assert (tulos["korkeus"], tulos["leveys"]) == (len(tulos["karttadata"][0]), len(tulos["karttadata"]))
    
    def oikeat_elementit(self, luo_käsittelijä, testitiedosto):
        tulos = luo_käsittelijä.käsittele_karttatiedosto(testitiedosto[0])
        print(tulos["karttadata"])

    def test_iso_kartta(self, luo_käsittelijä, testitiedosto):
        käsittelijä = luo_käsittelijä
        tulos = käsittelijä.käsittele_karttatiedosto(testitiedosto[1])
        assert (tulos["korkeus"], tulos["leveys"]) == (844, 868)

    
    def test_testidata(self, luo_käsittelijä, testiscen):
        tulos = luo_käsittelijä.parse_testi(testiscen)
        haluttu = {"kartta":"arena.map", "w":49, "h":49, "x1":19, "y1":26, "x2":19, "y2":29, "etäisyys":3.00000000}
        assert tulos[0] == haluttu

    def test_testidata_käsittelee_kaikki_rivit(self, luo_käsittelijä, testiscen):
        tulos = len(luo_käsittelijä.parse_testi(testiscen))
        assert tulos == 130
"""
    def test_parse_oikein(self, luo_käsittelijä, testitiedosto):
        käsittelijä = luo_käsittelijä
        tulos = käsittelijä.käsittele_karttatiedosto(testitiedosto[0])
        assert (tulos ==)
"""