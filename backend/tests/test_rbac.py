import unittest
from app import create_app

class TestRBAC(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_casting_assistant_access(self):
        response = self.client.get('/api/actors', headers={'Authorization': 'Bearer casting_assistant_token'})
        self.assertEqual(response.status_code, 200)

    def test_executive_producer_access(self):
        response = self.client.post('/api/movies', json={'title': 'New Movie', 'release_date': '2024-11-30'}, headers={'Authorization': 'Bearer executive_producer_token'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
