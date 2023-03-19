from flask import Flask, render_template, redirect, session, request
from libreria.conexion import *

app = Flask(__name__)

app.secret_key = 'clave_secreta'
titulo = []


@app.route('/')
def security():
    if 'email' in session:
        return redirect('crear')
    else:
        return redirect('login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    content = {
        'titulo': 'Agenda Mongo',
        'subtitulo': 'Login'
    }

    if request.method == 'POST':
        email = request.form.get('email')
        contra = request.form.get('password')

        user, noRegistrado = loginUser(email)

        if user and noRegistrado == False:

            if user['email'] == email and user['password'] == contra:
                session['name'] = user['name']
                session['surname'] = user['surname']
                session['email'] = email
                return redirect('crear')
        else:
            error = True
            return render_template('login.html', error=error, **content)
    return render_template('login.html', **content)


@app.route('/register', methods=['GET', 'POST'])
def register():
    content = {
        'titulo': 'Agenda Mongo',
        'subtitulo': 'Registro Usuarios'
    }
    """
        Registra usuarios en la base de datos y comprueba que ese usuario no este.
    """
    if request.method == 'POST':
        nombre = request.form.get('name')
        apellido = request.form.get('apellidos')
        email = request.form.get('email')
        password = request.form.get('password')

        yaRegistrado = crearUsuario(nombre, apellido, email, password)

        if yaRegistrado:
            error = True
            return render_template('register.html', error=error, **content)
        else:
            return redirect('login')
    return render_template('register.html', **content)


@app.route('/crear', methods=['POST', 'GET'])
def index():
    content = {
        'titulo': 'Agenda Mongo',
        'subtitulo': 'Bienvenido'
    }

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        nota = request.form.get('nota')
        email = session['email']
        insertarNotas(titulo, email, nota)
    return render_template('index.html', **content)


@app.route('/ver')
def ver():
    content = {
        'titulo': 'Agenda',
        'subtitulo': 'Lista de notas'
    }
    email = session['email']
    session['notas'] = sacarNotas(email)
    return render_template('ver.html', **content)


@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        titulo.append(request.form.get('editar'))
        email = session['email']
        mensaje_nota = sacarNotasPorTitulo(titulo[0], email)
        session['notaEditar'] = mensaje_nota

        if request.form.get('editado'):
            nota = request.form.get('editado')
            email = session['email']
            editarNota(titulo[0], email, nota)
            titulo.clear()
            return redirect('ver')

    content = {
        'titulo': 'Agenda Mongo',
        'subtitulo': 'Editar Nota',
        'titulo_editar': titulo[0]
    }
    return render_template('editar.html', **content)


@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    titulo_editar = request.form.get('eliminar')
    borrarNotas(titulo_editar)
    return redirect('ver')

@app.route('/salir')
def salir():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
