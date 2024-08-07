from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Database_url = "postgresql://postgres:238383@localhost/blog_app"

engine = create_engine(Database_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
