import unittest
from src.notification import choisir_canal, demander_validation
class TestNotification(unittest.TestCase):
    def test_critical_teams(self):
        self.assertEqual(choisir_canal("CRITICAL"), "TEAMS")
    def test_high_teams(self):
        self.assertEqual(choisir_canal("HIGH"), "TEAMS")
    def test_medium_email(self):
        self.assertEqual(choisir_canal("MEDIUM"), "EMAIL")
    def test_low_dashboard(self):
        self.assertEqual(choisir_canal("LOW"), "DASHBOARD")
    def test_criticite_inconnue(self):
        with self.assertRaises(ValueError):
            choisir_canal("URGENT")
    def test_validation_non_sensible(self):
        self.assertTrue(demander_validation(False, "non"))
    def test_validation_sensible(self):
        self.assertTrue(demander_validation(True, " OUI "))
        self.assertFalse(demander_validation(True, "non"))