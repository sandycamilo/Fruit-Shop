# tests.py

from unittest import TestCase, main as unittest_main
from app import app

class FruitShopTests(TestCase):
    """Flask tests."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_index(self):
        """Test the fruits homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Fruit', result.data)

if __name__ == '__main__':
    unittest_main()