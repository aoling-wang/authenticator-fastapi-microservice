from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base

# Define the User entry blueprint for the database, creating the users table with the columns: id, email, and hashed password

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )