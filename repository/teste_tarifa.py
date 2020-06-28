import unittest
import requests
import tarifas

class TesteTarifas(unittest.TestCase):
    def teste_find_all_ddds(self):
        result = ['011', '016', '017', '018']
        self.assertEqual(tarifas.find_all_ddds(), result)

    def teste_find_valor_string(self):
        result = 1.9
        self.assertEqual(tarifas.find_valor('011', '016'), result)

    def teste_find_valor_int(self):
        result = []
        self.assertEqual(tarifas.find_valor(123, 6321), result)

    def teste_find_valor_int_negativa(self):
        result = []
        self.assertEqual(tarifas.find_valor(-123, -6321), result)

    def teste_find_valor_incorrect_string(self):
        result = []
        self.assertEqual(tarifas.find_valor('asdf', '01df6s'), result)

    def teste_find_valor_string_equals(self):
        result = []
        self.assertEqual(tarifas.find_valor('011', '011'), result)

if __name__ == "__main__":
    unittest.main()
