import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import repository.planos as planos_repo
import repository.tarifas as tarifas_repo
import service.planos as planos_service
import service.tarifas as tarifas_service
import service.calcular_valor_da_chamada as cvc_service
