from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import User
from app.core.security import { hash_password, verify_password }
from app.schemas.auth import { UserRegister, UserLogin }

# Creates the user if they don't already exist in database, 
# hashes the password, and stores the new user in the database.
# (Registration process)

def create_user(
    db: Session,
    user_data: UserRegister,
) -> User:
    existing_user = db.scalar(
        select(User).where(
            User.email == user_data.email.lower()
        )
    )

    if existing_user:
        raise ValueError("User already exists")

    user = User(
        email=user_data.email.lower(),
        password_hash=hash_password(user_data.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

# Authenticates the user by checking if they exist in the database 
# and checking their password.
# (Login process)

def authenticate_user(
    db: Session,
    login_data: UserLogin,
) -> User | None:
    user = db.scalar(
        select(User).where(
            User.email == login_data.email.lower()
        )
    )

    if not user:
        return None

    if not verify_password(
        login_data.password,
        user.password_hash,
    ):
        return None

    return user