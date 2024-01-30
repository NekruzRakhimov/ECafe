from flask import jsonify, Blueprint, request
import repository

app = Blueprint('routes', __name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"status": "server is up and running..."}), 200


@app.route('/orders', methods=["GET", "POST"]) #Nosir
def order_control():
    if request.method == 'GET':
        pass

    else:
        pass


@app.route('/users', methods=['GET', 'POST']) #Muhammad
def users():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route('/menu', methods=['GET', 'POST']) # Sasha
def menu():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route('/tables', methods=['GET', 'POST']) #Nosir
def tables():
    if request.method == 'GET':
        pass
    else:
        pass
