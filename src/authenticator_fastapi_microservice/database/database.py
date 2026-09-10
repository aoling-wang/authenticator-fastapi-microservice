from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings

class Base(DeclarativeBase):
    pass

# Establish connection to database using SQLAlchemy engine

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False},
)

# Create a session for database connection and interactions

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

# Connects to the database and yields a session for use in the application, ensuring proper closure of the session after use

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()