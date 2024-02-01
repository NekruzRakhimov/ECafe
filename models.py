from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship, DeclarativeBase
from connection import engine


class Base(DeclarativeBase):
    pass


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    description = Column(String(500))
    status = Column(String(100), nullable=False)
    status_time = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return (f"<Menu(id={self.id}, title={self.title}, description={self.description}, status={self.status}, "
                f"status_time={self.status_time}, price={self.price} )>")


class Personal(Base):
    __tablename__ = 'personal'
    id = Column(Integer, primary_key=True)
    job_title = Column(String(255), nullable=False)
    salary = Column(Float, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)
    status = Column(String(100), nullable=False)
    created_at = Column(DateTime)
    delete_at = Column(DateTime)
    is_deleted = Column(Boolean, default=False)

    def __repr__(self):
        return (f"<Personal(id={self.id}, job_title={self.job_title}, salary={self.salary}, "
                f"first_name={self.first_name}, last_name={self.last_name}, age={self.age}, status={self.status} )>")


class TableManagement(Base):
    __tablename__ = 'table_management'
    id = Column(Integer, primary_key=True)
    table_number = Column(Integer, nullable=False)
    personal_id = Column(Integer, ForeignKey('personal.id'))
    personal = relationship("Personal", backref="table_management")
    is_deleted = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<TableManagement(id={self.id}, table_number={self.table_number}, personal_id={self.personal_id})>"


class OrderManagement(Base):
    __tablename__ = 'order_management'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, unique=True)
    menu_id = Column(Integer, ForeignKey('menu.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    order_status = Column(String(50), nullable=False)
    dish_status = Column(String(50), nullable=False)
    table_management_id = Column(Integer, ForeignKey('table_management.id'), nullable=False)
    personal_id = Column(Integer, ForeignKey('personal.id'), nullable=False)
    menu = relationship("Menu", backref="order_management")
    created_at = Column(DateTime)
    is_deleted = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return (f"<OrderManagement(id={self.id}, order_status={self.order_status}, dish_status={self.dish_status}"
                f"table_management_id={self.table_management_id})>")


Base.metadata.create_all(bind=engine)
