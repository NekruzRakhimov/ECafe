from sqlalchemy import and_
from models import Menu, Personal, OrderManagement, TableManagement
from connection import engine
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime


class Repository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_personal(self):
        return self.session.query(Personal).all()

    def add_personal(self, job_title, salary, first_name, last_name, age, status, created_at, delete_at):
        personal = Personal(job_title=job_title, salary=salary, first_name=first_name, last_name=last_name, age=age,
                            status=status)
        self.session.add(personal)
        self.session.commit()
        return personal

    def delete_personal(self, personal_id):
        personal = self.session.query(Personal).filter_by(id=personal_id).first()
        if personal:
            self.session.delete(personal)
            self.session.commit()
            return personal
        else:
            raise ValueError("Personal data not found")

    def set_personal(self, personal_id, new_role):
        personal = self.session.query(Personal).filter_by(id=personal_id).first()
        if personal:
            personal.job_title = new_role
            self.session.commit()
            return personal
        else:
            "The data has not been updated"
