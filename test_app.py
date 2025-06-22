import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_home_page(self):
        """Test that the home page returns 'Hello, World!'"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')
        
    def test_api_hello(self):
        """Test that the API endpoint returns correct JSON"""
        response = self.app.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'hello world'})

if __name__ == '__main__':
    unittest.main() 