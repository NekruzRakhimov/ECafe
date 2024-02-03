from flask import jsonify, Blueprint, request
from repository import *
from connection import get_session

app = Blueprint('routes', __name__)


@app.route('/')
def index():
    return "Raising the server"


#  =====================================================================================================================

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    session = get_session()

    if request.method == 'GET':
        dishes = get_menu(session)
        serialized_dishes = [{"id": dish.id, "title": dish.title, "description": dish.description,
                              "status": dish.status, "status_time": dish.status_time, "price": dish.price}
                             for dish in dishes]
        return jsonify({"menu": serialized_dishes}), 200

    elif request.method == 'POST':
        data = request.get_json()
        title = data['title']
        description = data['description']
        status = data['status']
        status_time = data['status_time']
        price = data['price']

        dish = create_dish(session, title, description, status, status_time, price)
        serialized_dish = {"id": dish.id, "title": dish.title, "description": dish.description,
                           "status": dish.status, "status_time": dish.status_time, "price": dish.price}

        return jsonify({"dish": serialized_dish}), 201
    else:
        return jsonify({"error": "Method Not Allowed"}), 405


@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def delete_dish_route(dish_id):
    session = get_session()
    deleted_dish = delete_dish(session, dish_id)
    if deleted_dish:
        return jsonify({"message": f"Dish with id {dish_id} deleted successfully."})
    return jsonify({"error": f"Dish with id {dish_id} not found."}), 404


@app.route('/price/<int:dish_id>', methods=['PATCH'])
def price_change(dish_id):
    data = request.get_json()
    new_price = data['price']
    price_change(dish_id, new_price)
    return jsonify({"message": f"Price of dish with id {dish_id} changed successfully."}), 200


@app.route('/status/<int:dish_id>', methods=['PATCH'])
def status_change(dish_id):
    status_change(dish_id)
    return jsonify({"message": f"Status of dish with id {dish_id} changed successfully."}), 200


#  =====================================================================================================================

@app.route('/users', methods=['GET', 'POST'])
def users():
    session = get_session()
    if request.method == 'GET':
        all_personal = get_all_personal(session)
        personal_json = [
            {"id": person.id, "job_title": person.job_title, "salary": person.salary, "first_name": person.first_name,
             "last_name": person.last_name, "age": person.age, "status": person.status,
             "created_at": person.created_at, "delete_at": person.delete_at} for person in all_personal]
        return jsonify({"personal": personal_json})

    elif request.method == 'POST':
        data = request.get_json()
        job_title = data.get('job_title')
        salary = data.get('salary')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        age = data.get('age')
        status = data.get('status')

        personal = add_personal(session, job_title, salary, first_name, last_name, age, status)
        print("PERSON: ", personal)
        return data
    else:
        return jsonify({"error": "Method Not Allowed"}), 405


@app.route('/users/<int:personal_id>', methods=['DELETE'])
def delete_personal_route(personal_id):
    session = get_session()
    deleted_personal = delete_personal(session, personal_id)
    if deleted_personal:
        return jsonify({"message": f"Personal with id {personal_id} deleted successfully."})
    return jsonify({"error": f"Personal with id {personal_id} not found."}), 404


@app.route('/users/<int:personal_id>/role', methods=['PATCH'])
def set_personal_role(personal_id):
    session = get_session()
    data = request.get_json()
    new_role = data.get('role')

    updated_personal = set_personal(session, personal_id, new_role)
    if updated_personal:
        return jsonify({"message": f"Role for Personal with id {personal_id} set to {new_role}."})
    return jsonify({"error": f"Personal with id {personal_id} not found."}), 404

#  =====================================================================================================================
