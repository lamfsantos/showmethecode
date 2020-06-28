import unittest
import requests
import planos

class TestePlanos(unittest.TestCase):
    def teste_find_all(self):
        result = [('Fale mais 30', 30), ('Fale mais 60', 60), ('Fale mais 120', 120)]
        self.assertEqual(planos.find_all(), result)

    def teste_find_by_minutes_30(self):
        result = [('Fale mais 30', 30)]
        self.assertEqual(planos.find_by_minutos(30), result)

    def teste_find_by_minutes_45(self):
        result = []
        self.assertEqual(planos.find_by_minutos(45), result)

    def teste_find_by_minutes_negative(self):
        result = []
        self.assertEqual(planos.find_by_minutos(-3), result)

    def teste_find_by_minutes_string(self):
        result = [('Fale mais 30', 30)]
        self.assertEqual(planos.find_by_minutos("30"), result)

if __name__ == "__main__":
    unittest.main()
