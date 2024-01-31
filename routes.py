from flask import jsonify, Blueprint, request
from sqlalchemy.orm import Session

from repository import Repository
from ECafe.models import Menu

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
        session = Session
        repository = Repository(session)
        dishes = repository.get_menu()
        serialized_dishes = []

        for dish in dishes:
            dish_dict = dish.__dict__
            del dish_dict["_sa_instance_state"]
            serialized_dishes.append(dish_dict)

        return {"menu": serialized_dishes}, 200
    elif request.method == 'POST':
        data = request.get_json()
        dish = Menu(title=data['title'], )



@app.route('/tables', methods=['GET', 'POST']) #Nosir
def tables():
    if request.method == 'GET':
        pass
    else:
        pass
