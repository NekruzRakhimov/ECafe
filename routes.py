from flask import jsonify, Blueprint, request
from sqlalchemy.orm import sessionmaker
import repository
from connection import engine
from repository import Repository, sessionmaker

app = Blueprint('routes', __name__)


@app.route('/', methods=["GET"])
def index():
    return jsonify({"status": "server is up and running..."}), 200


@app.route('/orders', methods=["GET", "POST"])  # Nosir
def order_control():
    if request.method == 'GET':

        pass

    else:
        pass


# Muhammad ---------------------------------------------------------------------------------------


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        all_personal = repository.get_all_personal()
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

        personal = repository.add_personal(job_title, salary, first_name, last_name, age, status)
        return jsonify({"id": personal.id, "job_title": personal.job_title,
                        "first_name": personal.first_name, "last_name": personal.last_name,
                        "age": personal.age}), 201

    return jsonify({"error": "Invalid request method"}), 400


@app.route('/users/<int:personal_id>', methods=['DELETE'])
def delete_personal(personal_id):
    deleted_personal = repository.delete_personal(personal_id)
    if deleted_personal:
        return jsonify({"message": f"Personal with id {personal_id} deleted successfully."})
    return jsonify({"error": f"Personal with id {personal_id} not found."}), 404


@app.route('/users/<int:personal_id>/role', methods=['PATCH'])
def set_personal_role(personal_id):
    data = request.get_json()
    new_role = data.get('role')

    updated_personal = repository.set_personal_role(personal_id, new_role)
    if updated_personal:
        return jsonify({"message": f"Role for Personal with id {personal_id} set to {new_role}."})
    return jsonify({"error": f"Personal with id {personal_id} not found."}), 404


# Muhammad ---------------------------------------------------------------------------------------

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
