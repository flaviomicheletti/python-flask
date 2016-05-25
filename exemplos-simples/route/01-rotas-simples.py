# coding: utf-8
from flask import Flask
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
@app.route('/clientes/')
def listar_clientes():
    return "/clientes"

#
# Rota para /clientes/1, /clientes/2, /clientes/3
#
@app.route('/clientes/<int:id>')
def retorna_cliente(id):
    return '/clientes/%d' % id

if __name__ == '__main__':
    app.debug = True
    app.run()
