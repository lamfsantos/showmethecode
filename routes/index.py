from flask import Blueprint, render_template
import service.tarifas as tarifas
import service.planos as planos

index_blueprint = Blueprint("index", __name__, static_folder="static", template_folder="templates")

@index_blueprint.route('/')
def index():
    return render_template("index.html", ddds = tarifas.find_all_ddds(), planos = planos.find_all())
