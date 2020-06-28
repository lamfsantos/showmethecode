from flask import Flask
from routes.index import index_blueprint
from routes.resultado import resultado_blueprint

app = Flask(__name__)
app.register_blueprint(resultado_blueprint)
app.register_blueprint(index_blueprint)

if __name__ == "__main__":
    app.run()
