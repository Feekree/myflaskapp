import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), "Hello, Flask!")

    def test_status(self):
        tester = app.test_client(self)
        response = tester.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "OK"})

if __name__ == "__main__":
    unittest.main()
