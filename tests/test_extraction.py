import unittest
from src.extraction import masquer_secrets
class TestExtraction(unittest.TestCase):
    def test_password(self):
        self.assertEqual(masquer_secrets("db password=abc123 ok"),
                         "db password=[SECRET] ok")
    def test_bearer(self):
        self.assertEqual(masquer_secrets("Authorization: Bearer eyJhbGciOi"),
                         "Authorization: Bearer [SECRET]")