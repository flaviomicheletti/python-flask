# coding: utf-8
from flask import Flask, url_for, request
app = Flask(__name__)

#
# Rota para /
#
@app.route('/')
def home():
    return 'home'

#
# Rota para /clientes
#
@app.route('/clientes/', methods=['GET', 'POST'])
def listar_clientes():

    #
    # Create
    #
    if request.method == 'POST':
        return "POST to /clientes: inserir cliente"

    #
    # Read
    #
    elif request.method == 'GET':
        return "GET to /clientes: listar clientes"

    # erro
    else:
        return "método desconhecido para /clientes"

#
# Rota para /clientes/1, /clientes/2, /clientes/3
#
@app.route('/clientes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def retorna_cliente(id):

    #
    # Read
    #
    if request.method == 'GET':
        return "GET to /clientes: recuperar um cliente id=%d" % id

    #
    # Update
    #
    elif request.method == 'PUT':
        return "PUT to /clientes: atualizar um cliente id=%d" % id

    #
    # Delete
    #
    elif request.method == 'DELETE':
        return "DELETE to /clientes: deletar um cliente id=%d" % id

    # erro
    else:
        return "método desconhecido para /clientes/<id>"


if __name__ == '__main__':
    app.debug = True
    app.run()
