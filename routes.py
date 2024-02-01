from flask import jsonify, Blueprint, request
from ECafe.models import Menu
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
            if time > 0:
                status = "Готовится"
            else:
                status = "Готово"
            return status

        data = request.get_json()
        status_time = data['status_time']
        dish = Menu(title=data['title'],
                    description=data['description'],
                    status=get_status(status_time),
                    status_time=status_time,
                    price=data['price'])
        repository.create_dish(dish)
        return {"status": "dish created"}, 201


@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    repository.delete_dish(dish_id)
    return jsonify({"message": f"Menu with id {dish_id} deleted successfully."}), 200


@app.route('/price/<int:dish_id>', methods=['PATCH'])
def price_change(dish_id):
    data = request.get_json()
    new_price = data['price']
    repository.price_change(dish_id, new_price)
    return jsonify({"message": f"Price of dish with id {dish_id} changed successfully."}), 200


@app.route('/status/<int:dish_id>', methods=['PATCH'])
def status_change(dish_id):
    repository.status_change(dish_id)
    return jsonify({"message": f"Status of dish with id {dish_id} changed successfully."}), 200
