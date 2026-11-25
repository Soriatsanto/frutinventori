from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/soriats"
DATABASE_URL="postgresql+psycopg2://frutiess_user:HkiblL1aI38O9eP3Dh0MfRfWaq76tJJd@dpg-dc3aoqifngtc73dfnf5g-a.oregon-postgres.render.com/frutiess"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
