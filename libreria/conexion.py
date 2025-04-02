from flask import session
from pymongo import MongoClient
import datetime
from dotenv import load_dotenv
import os

# Cargamos variable del archivo .env
load_dotenv()

MONGO_URL_ATLAS = os.getenv("MONGO_URL_ATLAS")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

client = MongoClient(MONGO_URL_ATLAS, connect=True)

db = client[MONGO_DATABASE]

def insertarNotas(titulo, email, nota):
    """
        Inserta notas en la base de datos.
    """
    collection = db['notas']
    nota = {
        'email': email,
        'titulo': titulo,
        'fecha': datetime.datetime.now().strftime("%d/%m/%Y"),
        'nota': nota
    }

    collection.insert_one(nota)


def borrarNotas(titulo):
    """
        Elimina las palabras de la base de datos.
    """
    collection = db['notas']
    collection.delete_one({'titulo': titulo})


def sacarNotas(email):
    """        
        Saca las notas de la base de datos.
    """
    collection = db['notas']
    notas = []
    resultados = collection.find({'email': email}, {'_id': 0})

    for documento in resultados:
        notas.append({
            'titulo': documento['titulo'],
            'nota': documento['nota'],
            'fecha': documento['fecha']
        })
    return notas


def sacarNotasPorTitulo(titulo, email):
    """        
        Saca las notas de la base de datos.
    """
    collection = db['notas']
    notas = []
    resultados = collection.find(
        {'titulo': titulo, 'email': email}, {'_id': 0})

    for documento in resultados:
        notas.append(documento['nota'])
    return notas


def editarNota(titulo, email, nota):
    """
        Edita notas en la base de datos.
    """
    collection = db['notas']
    collection.update_one({'titulo': titulo, 'email': email}, {
                          '$set': {'nota': nota}})


# Parte de gestión de usuarios

def crearUsuario(nombre, apellido, email, password):
    # Comprobacion de que el usuario no existe
    collection = db['users']
    user = []
    resultados = collection.find_one({'email': email}, {'_id': 0})
    
    if resultados != None:
        for documento in resultados:
            user.append(documento)

    if len(user) == 0:
        yaRegistrado = False
    else:
        yaRegistrado = True

    # Si el usuario no existe lo registramos

    if yaRegistrado == False:
        collection.insert_one(
            {'name': nombre, 'surname': apellido, 'email': email, 'password': password})

    return yaRegistrado


def loginUser(email):
    collection = db['users']
    user = {}
    resultados = collection.find(
        {'email': email}, {'_id': 0, 'name': 1, 'surname':1, 'password': 1, 'email': 1})

    for documento in resultados:
        user.update(
            {'email': documento['email'], 'name': documento['name'], 'surname': documento['surname'], 'password': documento['password']})

    if user == '{}':
        noRegistrado = True
    else:
        noRegistrado = False
    return user, noRegistrado
