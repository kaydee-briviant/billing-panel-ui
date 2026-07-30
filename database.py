from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = 'admin'
PASSWORD = "password"
HOST = "localhost"
PORT = "3306"
DATABASE = "test_database"

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

def get_sessions():
    return SessionLocal()
