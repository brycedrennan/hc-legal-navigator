import unittest
from app.main import app


class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"LegalNavigator", response.data)

    def test_about(self):
        response = self.app.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"LegalNavigator", response.data)


if __name__ == "__main__":
    unittest.main()
