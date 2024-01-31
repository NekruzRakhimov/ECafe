from flask import jsonify, Blueprint, request
import repository
from repository import *

app = Blueprint('routes', __name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"status": "server is up and running..."}), 200


@app.route('/orders', methods=["GET", "POST"])  # Nosir
def order_control():
    if request.method == 'GET':
        pass

    else:
        data = request.get_json()
        try:
            orders_add(data['menu'], data['personal_id'], data['table_id'])
            return {'status': 'Success'}, 201
        except:
            return {'status': 'Something went wrong please check your data and send back.'}, 404


@app.route('/users', methods=['GET', 'POST'])  # Muhammad
def users():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route('/menu', methods=['GET', 'POST'])  # Sasha
def menu():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route('/tables', methods=['GET', 'POST'])  # Nosir
def tables():
    if request.method == 'GET':
        pass
    else:
        pass
