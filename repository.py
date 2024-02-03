from flask import jsonify
from sqlalchemy import and_
from sqlalchemy.orm import Session
from models import Menu, Personal
from connection import engine
from datetime import datetime

import logging


#  =====================================================================================================================

def get_menu(session: Session):
    return session.query(Menu).filter(Menu.is_deleted == False).all()


def create_dish(db: Session, title: str, description: str, status: str, status_time: int, price: float):
    try:
        dish = Menu(title=title, description=description, status=status, status_time=status_time, price=price)
        db.add(dish)
        db.commit()
        return dish
    except Exception as e:
        logging.error(f"Error: {e}")
        return str(e)


def delete_dish(_id):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(id == _id).first()
        if dish:
            db.delete(dish)
            db.commit()
            return dish
        else:
            raise ValueError("Dish data not found")


def price_change(_id, new_price):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(and_(Menu.id == _id)).first()
        if dish:
            dish.price = new_price
            db.add(dish)
            db.commit()
            return dish
        else:
            raise ValueError("Menu data not found")


def status_change(_id):
    with Session(autoflush=False, bind=engine) as db:
        dish = db.query(Menu).filter(and_(Menu.id == _id)).first()
        if dish:
            dish.status = "Готово"
            dish.status_time = 0
            db.add(dish)
            db.commit()
            return dish
        else:
            raise ValueError("Menu data not found")


#  =====================================================================================================================

def get_all_personal(session):
    return session.query(Personal).all()


def add_personal(db, job_title, salary, first_name, last_name, age, status):
    try:

        personal = Personal(job_title=job_title, salary=salary, first_name=first_name, last_name=last_name, age=age,
                            status=status)
        db.add(personal)
        db.commit()
        return personal
    except Exception as e:
        logging.error(f"ERRPR is: {e}")
        return str(e)


def delete_personal(session, personal_id):
    personal = session.query(Personal).filter_by(id=personal_id).first()
    if personal:
        session.delete(personal)
        session.commit()
        return personal
    else:
        raise ValueError("Personal data not found")


def set_personal(session, personal_id, new_role):
    personal = session.query(Personal).filter_by(id=personal_id).first()
    if personal:
        personal.job_title = new_role
        session.commit()
        return personal
    else:
        return "The data has not been updated"

#  =====================================================================================================================
