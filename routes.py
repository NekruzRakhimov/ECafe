from datetime import datetime

from flask import jsonify, Blueprint, request
import repository
from ECafe.models import Menu
from connection import get_session

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
        dishes = repository.get_menu()
        serialized_dishes = []
        for dish in dishes:
            dish_dict = dish.__dict__
            del dish_dict["_sa_instance_state"]
            serialized_dishes.append(dish_dict)
        return {"menu": serialized_dishes}, 200

    elif request.method == 'POST':
        def get_status(time):
            if time is not None:
                status = "Expectation"
            else:
                status = "Done"
            return status

        data = request.get_json()
        status_time = datetime.now()
        dish = Menu(title=data['title'],
                    description=data['description'],
                    status=get_status(status_time),
                    status_time=status_time,
                    price=data['price'])
        repository.create_dish(dish)
        return {"status": "dish created"}, 201


@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_dish(id):
    session = get_session()
    deleted_menu = repository.delete_dish(session, id)
    if deleted_menu:
        return jsonify({"message": f"Personal with id {id} deleted successfully."}), 200
    return jsonify({"error": f"Personal with id {id} not found."}), 404







@app.route('/tables', methods=['GET', 'POST']) #Nosir
def tables():
    if request.method == 'GET':
        pass
    else:
        pass
