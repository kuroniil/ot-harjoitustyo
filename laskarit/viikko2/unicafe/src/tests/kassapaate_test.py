import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_luodun_kassapaatteen_myydyt_lounaat_on_oikea(self):
        self.assertEqual(self.kassapaate.myydyt_lounaat(), 0)

    def test_edullisten_lounaiden_osto_toimii_riittavalla_kateiseslla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisten_lounaiden_osto_toimii_riittamattomalla_kateisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_lounaiden_osto_toimii_riittavalla_kateiseslla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaiden_lounaiden_osto_toimii_riittamattomalla_kateisella(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisten_osto_toimii_kun_kortilla_riittava_saldo(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertEqual(self.kassapaate.myydyt_lounaat(), 1)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisten_osto_toimii_kun_kortilla_ei_riita_saldo(self):
        maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
        self.assertEqual(self.kassapaate.myydyt_lounaat(), 0)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_maukkaiden_osto_toimii_kun_kortilla_riittava_saldo(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(self.kassapaate.myydyt_lounaat(), 1)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_osto_toimii_kun_kortilla_ei_riita_saldo(self):
        maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))
        self.assertEqual(self.kassapaate.myydyt_lounaat(), 0)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahan_lataaminen_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001)
        self.assertEqual(self.maksukortti.saldo_euroina(), 11)

    def test_negatiivisen_summan_lataaminen_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)