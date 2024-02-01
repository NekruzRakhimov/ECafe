from datetime import datetime
from flask import jsonify, Blueprint, request
from ECafe.models import Menu
from connection import get_session
import repository

app = Blueprint('routes', __name__)


@app.route('/')
def index():
    return "Raising the server"


@app.route('/menu', methods=['GET', 'POST'])  # Sasha
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
    deleted_menu = repository.delete_dish(id)
    if deleted_menu:
        return jsonify({"message": f"Personal with id {id} deleted successfully."}), 200
    return jsonify({"error": f"Personal with id {id} not found."}), 404

