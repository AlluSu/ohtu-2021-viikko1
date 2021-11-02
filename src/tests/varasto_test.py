import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_nolla_tilavuus_nollaa(self):
        self.varasto = Varasto(0)
        
        self.assertAlmostEqual(self.varasto.tilavuus, 0)
    
    def test_negatiivinen_tilavuus_nollaa(self):
        self.varasto = Varasto(-10)
        
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_saldo_nollaa(self):
        self.varasto = Varasto(10, -1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivista_lukua_ei_voi_ottaa_varastosta(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-2), 0)

    def test_otetaan_isompi_kuin_saldo(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(2), 0)
    
    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        maara = self.varasto.lisaa_varastoon(-1)

        self.assertIsNone(maara)

    def test_maara_enemman_kuin_mita_mahtuu_tayttaa_kokonaan(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_tiedot_tulostuu_oikein(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
        self.varasto.lisaa_varastoon(8)
        self.assertEqual(self.varasto.__str__(), "saldo = 8, vielä tilaa 2")

