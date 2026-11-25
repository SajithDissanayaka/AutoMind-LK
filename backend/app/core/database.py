from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=3,
    max_overflow=2,
    connect_args={"connect_timeout": 10}
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()