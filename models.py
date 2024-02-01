from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, DeclarativeBase
from connection import engine


# создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    description = Column(String(500))
    status = Column(String(100), nullable=False)
    status_time = Column(DateTime)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Menu(id={self.id}, title={self.title}, price={self.price})>"


class Personal(Base):
    __tablename__ = 'personal'
    id = Column(Integer, primary_key=True)
    job_title = Column(String(255), nullable=False)
    salary = Column(DECIMAL(10), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False)  # тут показывет: Уволился, Работает,
    # created_at = Column(TIMESTAMP, server_default=func.now(), default=func.now())
    created_at = Column(DateTime)
    delete_at = Column(DateTime)

    def __repr__(self):
        return f"<Personal(id={self.id}, job_title={self.job_title}, first_name={self.first_name}, last_name={self.last_name}, age={self.age})>"


class TableManagement(Base):
    __tablename__ = 'table_management'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    table = Column(String(255), nullable=False)
    personal_id = Column(Integer, ForeignKey('personal.id'))
    personal = relationship("Personal", backref="table_management")

    def __repr__(self):
        return f"<TableManagement(id={self.id}, number={self.number}, table={self.table}, personal_id={self.personal_id})>"


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

    def __repr__(self):
        return f"<OrderManagement(id={self.id}, menu_id={self.menu_id}, order_status={self.order_status}, dish_status={self.dish_status}, table_id={self.table_id})>"


Base.metadata.create_all(bind=engine)
