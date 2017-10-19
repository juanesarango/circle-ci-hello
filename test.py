import unittest
import json
from index import app


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.get_data()), {'hello': 'world CI in heroku!'})

if __name__ == '__main__':
    unittest.main()
