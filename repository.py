from flask import jsonify
from sqlalchemy.orm import Session
from models import Personal
from datetime import datetime

import logging


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
