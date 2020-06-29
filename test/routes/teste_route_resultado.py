import unittest
import requests

class TesteResultado(unittest.TestCase):
    def teste_resultado_esperado(self):
        response = requests.get("http://127.0.0.1:5000/resultado?ddd_origem=011&ddd_destino=011&minutos=1&plano=30")
        self.assertEqual(response.status_code, 200)

    def teste_resultado_ddd_inexistente(self):
        response = requests.get("http://127.0.0.1:5000/resultado?ddd_origem=00&ddd_destino=025&minutos=1&plano=30")
        self.assertEqual(response.status_code, 200)

    def teste_resultado_minutos_negativos(self):
        response = requests.get("http://127.0.0.1:5000/resultado?ddd_origem=011&ddd_destino=016&minutos=-5&plano=30")
        self.assertEqual(response.status_code, 200)

    def teste_resultado_plano_inexistente(self):
        response = requests.get("http://127.0.0.1:5000/resultado?ddd_origem=011&ddd_destino=016&minutos=1&plano=20")
        self.assertEqual(response.status_code, 200)

    def teste_resultado_nenhum_parametro(self):
        response = requests.get("http://127.0.0.1:5000/resultado")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
