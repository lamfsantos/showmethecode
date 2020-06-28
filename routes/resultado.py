from flask import Blueprint, render_template, request
import service.calcular_valor_da_chamada as valor_chamada

resultado_blueprint = Blueprint("resultado", __name__, static_folder="static", template_folder="templates")

@resultado_blueprint.route('/resultado')
def index():
    ddd_origem = request.args.get('ddd_origem')
    ddd_destino = request.args.get('ddd_destino')
    minutos = request.args.get('minutos')
    plano = request.args.get('plano')

    if ddd_origem == ddd_destino:
        return render_template("ddds_iguais.html")

    return render_template("resultado.html", valor_chamada = valor_chamada.calcular_valor_chamada(ddd_origem, ddd_destino, minutos, plano))

#ddd_origem=011&ddd_destino=011&minutos=1&plano=30
