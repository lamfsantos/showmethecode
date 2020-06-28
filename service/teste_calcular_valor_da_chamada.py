import unittest
import calcular_valor_da_chamada as cvc

class TestePlanos(unittest.TestCase):
    def teste_find_all(self):
        result = {'sem_plano': 190.0, 'com_plano': 146.3}
        self.assertEqual(cvc.calcular_valor_chamada('011', '016', 100, 30), result)

if __name__ == "__main__":
    unittest.main()
