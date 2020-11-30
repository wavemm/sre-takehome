from hello import app
from unittest import TestCase

app.config['TESTING'] = True

class Test(TestCase):
    def testBasic(self):
        with app.test_client() as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, b"Hello, World!")

