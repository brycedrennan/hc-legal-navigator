import unittest
from app.models import LegalNavigator


class TestLegalNavigator(unittest.TestCase):
    def setUp(self):
        self.legal_navigator = LegalNavigator()

    def test_get_legal_advice(self):
        legal_advice = self.legal_navigator.get_legal_advice()
        self.assertIsNotNone(legal_advice)

    def test_get_legal_resources(self):
        legal_resources = self.legal_navigator.get_legal_resources()
        self.assertIsNotNone(legal_resources)

    def test_get_legal_updates(self):
        legal_updates = self.legal_navigator.get_legal_updates()
        self.assertIsNotNone(legal_updates)


if __name__ == "__main__":
    unittest.main()
