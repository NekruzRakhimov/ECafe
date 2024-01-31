from sqlalchemy import and_
from models import Menu, Personal, OrderManagement, TableManagement
from connection import engine
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime


def get_menu():
    with Session(autoflush=False, bind=engine) as db:
        return db.query(Menu).all()


def create_dish(dish):
    with Session(autoflush=False, bind=engine) as db:
        db.add(dish)
        db.commit()


def delete_dish(id):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(Menu.id == id).first()
        db.delete(dish)
        db.commit()
