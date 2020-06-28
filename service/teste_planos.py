import unittest
import requests
import planos

class TestePlanos(unittest.TestCase):
    def teste_find_all(self):
        result = [('Fale mais 30', 30), ('Fale mais 60', 60), ('Fale mais 120', 120)]
        self.assertEqual(planos.find_all(), result)

if __name__ == "__main__":
    unittest.main()
