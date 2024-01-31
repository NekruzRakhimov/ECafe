from sqlalchemy import create_engine

# db_url = 'postgresql://username:password@host:port/dbname'
db_url = 'postgres://eovqbhzz:OnGBM6Eza9hK6X2u2KGFeCAfmrIMsrM_@kesavan.db.elephantsql.com/eovqbhzz'

# создание машины соединения
engine = create_engine(db_url, echo=False)
