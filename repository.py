from sqlalchemy import and_
from models import Menu, Personal, OrderManagement, TableManagement
from connection import engine
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime
