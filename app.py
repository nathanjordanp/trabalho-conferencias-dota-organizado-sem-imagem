from flask import Flask, render_template
from objeto import Conferencias

listadeconferencias = [
    Conferencias(1, 'Dark willow', 'meu main hero', 'todo dia toda hora', 'no dotinha'),
    Conferencias(2, 'Marci', 'Meu segundo main hero', 'nem sempre da', 'no dotinha novamente'),
    Conferencias(3, 'Bane', 'Devia usar mais', 'as vezes quando to perdendo muito', 'novamente no doto')
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", listadeconferencias = listadeconferencias)

@app.route("/conferencias/<int:id>")
def funcaodota(id):
    for objeto in listadeconferencias:
        if objeto.get_id() == id:
            return render_template("conferencias.html", objeto = objeto)
