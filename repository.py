from sqlalchemy import and_
from models import Menu, Personal, OrderManagement, TableManagement
from connection import engine
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime


class Repository:
    def __init__(self, session: Session):
        self.session = session

    def get_menu(self):
        menu = self.session.query(Menu).all()
        return menu

    def create_dish(self, title, description, status_time, price):
        def get_status(time):
            if time > 0:
                return "Expectation"
            else:
                return "Done"

        status = get_status(status_time)
        menu = Menu(title=title, description=description, status=status, status_time=status_time, price=price)
        self.session.add(menu)
        self.session.commit()
        return menu
