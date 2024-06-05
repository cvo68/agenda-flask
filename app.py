from flask import Flask, json, render_template, redirect, url_for, request

app = Flask(__name__)

class Formulario:
    def __init__(self, dia, tarefa):
        self.dia = dia
        self.tarefa = tarefa

tarefas = []

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/salvar', methods = ["POST"])
def salvar():
    salvar = Formulario(request.form['dia'], request.form['tarefa'])
    
    request.form['dia']
    request.form['tarefa']
    
    tarefas.append(salvar)
    
    return render_template("lista.html", salvar =tarefas)
    
app.run(debug = True)