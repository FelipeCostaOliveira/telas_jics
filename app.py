from flask import Flask, render_template, request, redirect, url_for
from Classes import *
from cadastro import cadastro, cadastro_professor

app = Flask(__name__, template_folder='template', static_url_path='/static')
  # Use 'template' como o diretório de templates

# Define routes for student and professor registration
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        curso = request.form['curso']
        turma = request.form['turma']
        aluno = Aluno(nome, matricula, curso, turma)
        aluno.cadastrar_aluno(turma, curso)
    return render_template('cadastro_aluno.html')

@app.route('/cadastro_professor', methods=['GET', 'POST'])
def cadastrar_professor():
    if request.method == 'POST':
        nome = request.form['nome']
        matricula_prof = request.form['matricula_prof']
        senha = request.form['senha']
        servidor = professor(nome, matricula_prof, senha)
        servidor.cad_professor(senha)
    return render_template('cadastro_professor.html')

if __name__ == '__main__':
    app.run(debug=True)
