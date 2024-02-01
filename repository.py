from flask import jsonify
from sqlalchemy import and_
from sqlalchemy.orm import Session
from ECafe.connection import engine
from models import Menu
from datetime import datetime


def get_menu():
    with Session(autoflush=False, bind=engine) as db:
        return db.query(Menu).filter(is_deleted == False).all()


def create_dish(dish):
    with Session(autoflush=False, bind=engine) as db:
        db.add(dish)
        db.commit()


def delete_dish(_id):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(and_(id == _id, is_deleted == False)).first()
        if dish:
            dish.is_deleted = True
            db.add(dish)
            db.commit()
        else:
            raise ValueError("Personal data not found")

