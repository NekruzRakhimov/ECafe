from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# db_url = 'postgresql://username:password@host:port/dbname'
db_url = 'postgresql://eovqbhzz:OnGBM6Eza9hK6X2u2KGFeCAfmrIMsrM_@kesavan.db.elephantsql.com:5432/eovqbhzz'

# создание машины соединения
engine = create_engine(db_url, echo=False)
session = sessionmaker(autoflush=False, bind=engine)


def get_session():
    sess_db = session()
    try:
        return sess_db
    finally:
        sess_db.close()
