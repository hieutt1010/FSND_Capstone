import unittest
from app import create_app, db
from app.models import Actor

class TestActorsEndpoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()

    def test_get_actors(self):
        response = self.client.get('/api/actors')
        self.assertEqual(response.status_code, 200)

    def test_add_actor(self):
        response = self.client.post('/api/actors', json={
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male'
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
