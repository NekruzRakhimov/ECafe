from flask import jsonify, Blueprint, request
from sqlalchemy.orm import Session
from repository import get_all_personal, add_personal, delete_personal, set_personal
from connection import get_session
import repository
from repository import *


app = Blueprint('routes', __name__)


# def get_session():
#     return Session()

@app.route('/')
def index():
    return "Raising the server"


@app.route('/users', methods=['GET', 'POST'])
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

        personal = add_personal(
            session, job_title, salary, first_name, last_name, age, status)
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
