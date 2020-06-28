import service.tarifas as tarifas
import service.planos as planos

def calcular_valor_chamada(ddd_origem, ddd_destino, minutos, plano):
    valor_minuto = tarifas.find_valor(ddd_origem, ddd_destino)

    minutos = int(minutos)
    plano = int(plano)

    valor_sem_plano = minutos*valor_minuto

    if minutos <= plano:
        valor_com_plano = 0
    else:
        valor_com_plano = (minutos-plano)*valor_minuto
        valor_com_plano += valor_com_plano*0.10

    dict = {
        'sem_plano': valor_sem_plano,
        'com_plano': valor_com_plano
    }

    return dict
