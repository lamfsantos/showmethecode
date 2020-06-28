import repository.tarifas as tarifas

def find_all_ddds():
    return tarifas.find_all_ddds()

def find_valor(ddd_origem, ddd_destino):
    return tarifas.find_valor(ddd_origem, ddd_destino)
