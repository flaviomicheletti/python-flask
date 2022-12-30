# coding: utf-8
from flask import Flask, url_for, request

app = Flask(__name__)

#
# Route to/
#
@app.route("/")
def home():
    return "home"


#
# Route to /customers
#
@app.route("/customers/", methods=["GET", "POST"])
def customer_list():

    #
    # Create
    #
    if request.method == "POST":
        return "POST to /customers: inserir cliente"

    #
    # Read
    #
    elif request.method == "GET":
        return "GET to /customers: listar customers"

    # erro
    else:
        return "método desconhecido para /customers"


#
# Route to /customers/1, /customers/2, /customers/3
#
@app.route("/customers/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_customer(id):

    #
    # Read
    #
    if request.method == "GET":
        return "GET to /customers: get a customer id=%d" % id

    #
    # Update
    #
    elif request.method == "PUT":
        return "PUT to /customers: update a customer id=%d" % id

    #
    # Delete
    #
    elif request.method == "DELETE":
        return "DELETE to /customers: delete a customer id id=%d" % id

    # Error
    else:
        return "unknown method to /customers/<id>"


if __name__ == "__main__":
    app.debug = True
    app.run()
