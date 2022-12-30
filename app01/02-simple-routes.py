# coding: utf-8
from flask import Flask

app = Flask(__name__)

#
# Route to /
#
@app.route("/")
def home():
    return "home"


#
# Route to /customers
#
@app.route("/clientes/")
def customer_list():
    return "/customers"


#
# Route to /customers/1, /customers/2, /customers/3
#
@app.route("/customers/<int:id>")
def get_customer(id):
    return "/customers/%d" % id


if __name__ == "__main__":
    app.debug = True
    app.run()
