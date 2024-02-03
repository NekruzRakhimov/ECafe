from sqlalchemy import engine
from flask import Flask, jsonify
from sqlalchemy.orm import Session
from routes import app as routes_app

# from models import Base

# создаем таблицы
# Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.register_blueprint(routes_app)

if __name__ == '__main__':
    app.run(debug=True)