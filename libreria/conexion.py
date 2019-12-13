from flask import session
from pymongo import MongoClient
import datetime

MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)

db = client['agenda_mongo']

collection = db['notas']


def insertarNotas(titulo, nota):
    """
        Inserta notas en la base de datos.
    """
    nota = {
        'titulo': titulo,
        'fecha': datetime.datetime.now().strftime("%d/%m/%Y"),
        'nota': nota
    }

    collection.insert_one(nota)


def borrarNotas(titulo):
    """
        Elimina las palabras de la base de datos.
    """
    collection.delete_one({'titulo': titulo})


def sacarNotas():
    """        
        Saca las notas de la base de datos.
    """
    notas = []
    resultados = collection.find({}, {'_id': 0})

    for documento in resultados:
        notas.append({
            'titulo': documento['titulo'],
            'nota': documento['nota'],
            'fecha': documento['fecha']
        })
    return notas



def sacarNotasPorTitulo(titulo):
    """        
        Saca las notas de la base de datos.
    """
    notas = []
    resultados = collection.find({'titulo' : titulo}, {'_id': 0})

    for documento in resultados:
        notas.append(documento['nota'])
    return notas



def editarNota(titulo, nota):
    """
        Edita notas en la base de datos.
    """

    collection.update_one({'titulo': titulo}, {'$set': {'nota': nota}})
