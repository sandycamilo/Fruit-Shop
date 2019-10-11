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

    def test_selectfruit(self):
        """Test the select fruit page."""
        result = self.client.get('/fruits/selectfruit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'selectfruit', result.data)

    def test_checkout(self):
        """Test the checkout page."""
        result = self.client.get('/fruits/checkout')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'checkout', result.data)

    def test_tobasket(self):
        """Test the basket page."""
        result = self.client.get('/fruits/tobasket')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'tobasket', result.data)
    

if __name__ == '__main__':
    unittest_main()