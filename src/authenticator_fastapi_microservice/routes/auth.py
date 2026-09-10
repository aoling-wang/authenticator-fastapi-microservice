from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.auth import ( UserLogin, UserRegister, UserResponse )
from app.services.auth_service import ( authenticate_user, create_user )

# Creates an API router for authentication-related endpoints

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

# Processes user registration POST requests, validating the input data 
# and creating a new user in the database if they don't already exist. 
# Returns the created user's information or raises an HTTP exception if the user already exists.

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db),
):
    try:
        return create_user(db, user_data)

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error

# Processes user login POST requests, validating the input data
# and authenticating the user against the database.
# Returns the authenticated user's information or raises an HTTP exception if authentication fails.

@router.post(
    "/login",
    response_model=UserResponse,
)
def login(
    login_data: UserLogin,
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, login_data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return user