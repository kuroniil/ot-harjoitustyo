import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        # Negatiivisella summalla kasvattaminen ei toimi oikein,
        # vaatisi koodin muuttamista eikä se ilmeisesti ollut ideana
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(self.maksukortti.saldo, 1200)

    def test_ota_rahaa_toimii_oikein_kun_rahaa_riittavasti(self):
        self.maksukortti.ota_rahaa(900)

        self.assertEqual(self.maksukortti.saldo_euroina(), 1)

    def test_ota_rahaa_toimii_oikein_kun_rahaa_ei_riittavasti(self):
        self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_ota_rahaa_palauttaa_oikein_kun_raha_riittaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(900))

    def test_ota_rahaa_palauttaa_oikein_kun_raha_ei_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1100))

    def test_kortin_merkkijonoesitys_toimii_oikein(self):
        vastaus = str(self.maksukortti)
        self.assertEqual(vastaus, "Kortilla on rahaa 10.00 euroa")