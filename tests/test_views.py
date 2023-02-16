import unittest
from app.views import *


class TestViews(unittest.TestCase):
    def test_index(self):
        """Test the index view"""
        response = index()
        self.assertEqual(response.status_code, 200)
        self.assertIn("LegalNavigator", response.data)

    def test_search(self):
        """Test the search view"""
        response = search("legal question")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Legal Answer", response.data)


if __name__ == "__main__":
    unittest.main()
