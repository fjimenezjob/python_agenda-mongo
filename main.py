from flask import Flask, render_template, redirect, session, request
from libreria.conexion import *

app = Flask(__name__)

app.secret_key = 'clave_secreta'
titulo = []

@app.route('/', methods=['POST', 'GET'])
def index():
    content = {
        'titulo': 'Agenda Mongo',
        'subtitulo': 'Bienvenido'
    }

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        nota = request.form.get('nota')
        insertarNotas(titulo, nota)
    return render_template('index.html', **content)


@app.route('/ver')
def ver():
    content = {
        'titulo': 'Agenda',
        'subtitulo': 'Lista de notas'
    }
    session['notas'] = sacarNotas()
    return render_template('ver.html', **content)


@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        titulo.append(request.form.get('editar'))
        print(titulo)
        mensaje_nota = sacarNotasPorTitulo(titulo[0])
        session['notaEditar'] = mensaje_nota

        if request.form.get('editado'):
            nota = request.form.get('editado')
            editarNota(titulo[0], nota)
            titulo.clear()
            return redirect('ver')

    content = {
        'titulo': 'Agenda Mongo',
        'subtitulo': 'Editar Nota',
        'titulo_editar' : titulo[0]
    }
    return render_template('editar.html', **content)


@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    titulo_editar = request.form.get('eliminar')
    borrarNotas(titulo_editar)
    return redirect('ver')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)