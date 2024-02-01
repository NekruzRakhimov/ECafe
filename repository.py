from sqlalchemy import and_
from sqlalchemy.orm import Session
from ECafe.connection import engine
from models import Menu


def get_menu():
    with Session(autoflush=False, bind=engine) as db:
        return db.query(Menu).filter(Menu.is_deleted == False).all()


def create_dish(dish):
    with Session(autoflush=False, bind=engine) as db:
        db.add(dish)
        db.commit()


def delete_dish(_id):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(and_(Menu.id == _id, Menu.is_deleted == False)).first()
        if dish:
            dish.is_deleted = True
            db.add(dish)
            db.commit()
        else:
            raise ValueError("Menu data not found")


def price_change(_id, new_price):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(and_(Menu.id == _id, Menu.is_deleted == False)).first()
        if dish:
            dish.price = new_price
            db.add(dish)
            db.commit()
        else:
            raise ValueError("Menu data not found")


def status_change(_id):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(and_(Menu.id == _id, Menu.is_deleted == False)).first()
        if dish:
            dish.status = "Готово"
            dish.status_time = 0
            db.add(dish)
            db.commit()
        else:
            raise ValueError("Menu data not found")
