from flask import jsonify, Blueprint, request
import repository

app = Blueprint('routes', __name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"status": "server is up and running..."}), 200


@app.route('/orders', methods=["GET", "POST"])
def order_control():
    if request.method == 'GET':
        pass

    else:
        pass


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route('/tables', methods=['GET', 'POST'])
def tables():
    if request.method == 'GET':
        pass
    else:
        pass
