from flask import jsonify
from sqlalchemy.orm import Session
from models import Personal
from datetime import datetime
from connection import engine
from models import *
from sqlalchemy import and_

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

'----------start Orders-------------'
# adding orders to data


def orders_get_menu_info(_id):
    with Session(bind=engine, autoflush=False) as db:
        result = db.query(Menu).filter(Menu.id == _id).first()
        result = result.__dict__
        del result['_sa_instance_state']
        return result


def orders_add(menu_list, _personal_id, _table_id):
    """
    dict form of menu 
    [
        {menu_id : 1,
        amount:10},
        {menu_id: 2,
        amount:20}

    ]
    """
    with Session(bind=engine, autoflush=False) as db:
        _created_at = datetime.utcnow()
        _order_id = f'{datetime.now().day}{datetime.now().month}{datetime.now().year}{datetime.now().hour}{datetime.now().minute}'
        for i in menu_list:
            menu_info = orders_get_menu_info(i['menu_id'])
            _price = menu_info['price']
            _menu_id = i['menu_id']
            _amount = i['amount']
            _dish_status = menu_info['status']
            db.add(OrderManagement(created_at=_created_at,
                   order_id=_order_id, menu_id=_menu_id, amount=_amount, price=_price, total=_amount*_price, order_status='not yet', dish_status=_dish_status, table_id=_table_id, personal_id=_personal_id))
        db.commit()


def orders_actual(_personal_id=''):
    with Session(bind=engine, autoflush=False) as db:
        actual_order = db.query(OrderManagement).filter(and_(OrderManagement.order_status ==
                                                             'not yet', OrderManagement.order_status.ilike('%{}%'.format(_personal_id)))).all()
        orders_list = []
        for i in actual_order:
            i = i.__dict__
            del i['_sa_instance_state']
            orders_list.append(i)
    return orders_list


orders_add([{'menu_id': 1, 'amount': 3}], 0, 0)
print(orders_actual())
'----------end Orders--------------'
