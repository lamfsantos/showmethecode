from flask import Blueprint, render_template, request
import service.calcular_valor_da_chamada as valor_chamada
import service.planos as planos

resultado_blueprint = Blueprint("resultado", __name__, static_folder="static", template_folder="templates")

@resultado_blueprint.route('/resultado')
def index():
    minutos = request.args.get('minutos')
    ddd_origem = request.args.get('ddd_origem')
    ddd_destino = request.args.get('ddd_destino')
    plano = request.args.get('plano')

    if minutos is None or ddd_origem is None or ddd_destino is None or plano is None:
        return render_template("dados_faltantes.html")

    if ddd_origem == ddd_destino:
        return render_template("ddds_iguais.html")

    return render_template("resultado.html", valor_chamada = valor_chamada.calcular_valor_chamada(ddd_origem, ddd_destino, minutos, plano))
