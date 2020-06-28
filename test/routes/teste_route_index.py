import unittest
import requests

class TesteIndex(unittest.TestCase):
    def teste_index(self):
        response = requests.get("http://127.0.0.1:5000/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
