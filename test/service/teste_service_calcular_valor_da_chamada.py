import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from context import cvc_service

class TesteCVC(unittest.TestCase):
    def teste_valor_esperado(self):
        result = {'sem_plano': '190.00', 'com_plano': '146.30'}
        self.assertEqual(cvc_service.calcular_valor_chamada('011', '016', 100, 30), result)

    def teste_plano_inexistente(self):
        result = {}
        self.assertEqual(cvc_service.calcular_valor_chamada('011', '016', 100, 45), result)

    def teste_ddds_inexistentes(self):
         result = {}
         self.assertEqual(cvc_service.calcular_valor_chamada('0117', '06', 100, 30), result)

    def teste_minutos_negativos(self):
         result = {}
         self.assertEqual(cvc_service.calcular_valor_chamada('011', '016', -50, 30), result)

    def teste_minutos_string(self):
         result = {}
         self.assertEqual(cvc_service.calcular_valor_chamada('011', '016', 'jasdhf', 30), result)

if __name__ == "__main__":
    unittest.main()
